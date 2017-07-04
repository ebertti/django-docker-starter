# coding: utf-8
import os

from django.utils.deconstruct import deconstructible
from django.utils.text import slugify

from base.helper import gerar_hash


@deconstructible
class NomeArquivo(object):

    class Meta:
        verbose_name = "Arquivo"
        verbose_name_plural = "Arquivos"

    def __init__(self, pasta, *args):
        """
        Para ser utilizado no atributo upload_to de imagem, arquivo e qualquer outro que tenha path para upload
        :param pasta: nome da pasta
        :type pasta: str
        :param args: lista de atributos da instancia a ser utilizada para compor o nome do arquivo
        :type args: args of str
        """
        self.pasta = pasta
        self.args = args

    def __call__(self, instance, filename):
        """
        :param instance: instancia do model
        :type instance: Model
        :param filename: nome do arquivo
        :type filename: str
        :return: string formatada com os atributos ${pasta}/${atributos}_${uuid}.${extensao}
        :rtype: str
        """
        arquivoNome, arquivoExtensao = os.path.splitext(filename)
        arquivo = "_".join([slugify(getattr(instance, i))
                            for i in self.args
                            if getattr(instance, i)] + [slugify(arquivoNome)] + [gerar_hash()])
        arquivo += arquivoExtensao.lower()
        return os.path.join(self.pasta, arquivo)
