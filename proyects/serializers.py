from rest_framework import serializers
from .models import Proyect


class ProyectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyect
        fields = ('id', 'proyectos', 'rut',
                  'nombre_integrante', 'fec_creacion')
        read_only_fields = ('fec_creacion',)

    #CREAMOS UN METODO PARA VALIDAR RUT Y EVITAR DUPLICIDADES
    def validate_rut(self, value):
        if Proyect.objects.filter(rut=value).exists() and not self.instance:
            raise serializers.ValidationError(
                "El RUT ya está asociado a otro proyecto.")
        return value
    
    def create(self, validated_data):
        print("Creando un nuevo proyecto:", validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        print("Actualizando el proyecto:", instance,
              "con datos:", validated_data)
        return super().update(instance, validated_data)
