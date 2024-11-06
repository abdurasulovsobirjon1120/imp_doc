from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Section, File
from .serializers import SectionSerializer, DocumentSerializer


class SectionListCreateView(generics.ListCreateAPIView):
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Faqat hozirgi foydalanuvchiga tegishli bo‘lgan sectionlarni qaytaradi
        return Section.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Sectionni foydalanuvchiga tegishli qilib saqlaydi
        serializer.save(user=self.request.user)


class DocumentUploadView(generics.CreateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        section_id = self.request.data.get('section')
        file = self.request.FILES.get('file')

        # Fayl va section mavjudligini tekshirish
        if not file:
            raise NotFound('File is required.')

        # Frontenddan kiritilgan fayl nomi, turi va o'lchamini olish
        custom_file_name = self.request.data.get('file_name', file.name)
        custom_file_type = self.request.data.get('file_type', file.content_type)
        custom_file_size = self.request.data.get('file_size', file.size)

        try:
            # Faqat foydalanuvchiga tegishli sectionlarni topish
            section = Section.objects.get(id=section_id, user=self.request.user)
            serializer.save(
                section=section,
                file=file,
                file_name=custom_file_name,
                file_type=custom_file_type,
                file_size=custom_file_size,
                user=self.request.user
            )
        except Section.DoesNotExist:
            raise NotFound('Section not found or you do not have permission to access it.')



class DocumentUpdateView(generics.UpdateAPIView):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Faqat hozirgi foydalanuvchiga tegishli fayllarni qaytaradi
        return File.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        file = self.request.FILES.get('file')

        if file:
            # Agar yangi fayl yuklangan bo‘lsa, o‘lcham va turini yangilash
            serializer.save(
                file=file,
                file_name=file.name,
                file_type=file.content_type,  # Fayl turi
                file_size=file.size
            )
        else:
            # Agar fayl yuklanmasa, faqat boshqa maydonlarni yangilash
            serializer.save()
