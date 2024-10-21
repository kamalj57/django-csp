from rest_framework import serializers

class CSPReportSerializer(serializers.Serializer):
    document_uri = serializers.URLField(required=False)
    referrer = serializers.CharField(required=False)
    violated_directive = serializers.CharField(required=True)
    original_policy = serializers.CharField(required=True)
    blocked_uri = serializers.URLField(required=False, allow_blank=True)
    source_file = serializers.URLField(required=False, allow_blank=True)
    line_number = serializers.IntegerField(required=False)
    column_number = serializers.IntegerField(required=False)
