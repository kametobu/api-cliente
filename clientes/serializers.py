from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'Numero do CPF inválido'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome deve conter apenas carateres alfabetios'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'RG deve ter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Celular deve ter esse formato 00 00000-0000'})
        return data

    #def validate_cpf(self, cpf):
    #    if len(cpf) != 11:
    #        raise serializers.ValidationError('CPF deve ter 11 dígitos')
    #    return cpf
    #
    #def validate_nome(self, nome):
    #    if not nome.isalpha():
    #        raise serializers.ValidationError('Nome deve conter apenas carateres alfabetios')
    #    return nome
    #
    #def validate_rg(self, rg):
    #    if len(rg) != 9:
    #        raise serializers.ValidationError('RG deve ter 9 dígitos')
    #    return rg
    #
    #def validate_celular(self, celular):
    #    if len(celular) < 11:
    #        raise serializers.ValidationError('Celular deve ter 11 dígitos')
    #    return celular