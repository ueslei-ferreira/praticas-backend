import markdown
import language_tool_python
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    parser_classes = [JSONParser,MultiPartParser, FormParser]  # permite upload de arquivos

    def create(self, request, *args, **kwargs):
        file_obj = request.FILES.get("file")
        content = request.data.get("content")

        if file_obj and not content:
            content = file_obj.read().decode("utf-8")  # lê markdown e joga no banco

        serializer = self.get_serializer(data={
            "title": request.data.get("title"),
            "content": content
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def render(self, request, pk=None):
        note = self.get_object()
        html_content = markdown.markdown(note.content or "")
        return Response({"html": html_content})

    @action(detail=False, methods=['post'])
    def check_grammar(self, request):
        text = request.data.get("content", "")
        tool = language_tool_python.LanguageTool('pt-BR')
        matches = tool.check(text)
        suggestions = [
            {"message": m.message, "error": m.context, "suggestions": m.replacements}
            for m in matches
        ]
        return Response({"corrections": suggestions})
