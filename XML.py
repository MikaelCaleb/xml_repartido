# Importa o módulo os, que fornece funções para interagir com o sistema operacional, como manipulação de arquivos e diretórios.
import os
# Importa o módulo ElementTree do pacote xml, que é usado para analisar e criar arquivos XML.
import xml.etree.ElementTree as ET


# Define uma função chamada split_xml que recebe três parâmetros entre parenteses.
def split_xml(file_path, output_dir, tag_name):
    # Analisa o arquivo XML especificado por file_path e cria um objeto ElementTree.
    tree = ET.parse(file_path)
    # Obtém o elemento raiz do objeto ElementTree, que representa o documento XML.
    root = tree.getroot()

    # Encontra todos os elementos com a tag especificada.
    for elem in root.findall(tag_name):
        # Tenta encontrar o número da nota fiscal
        # Procura pelo subelemento Numero.
        numero_nota = elem.find('.//Numero')
        # Se Numero for encontrado, armazena seu texto em numero_nota. Caso contrário, numero_nota recebe 'sem_numero'.
        if numero_nota is not None:
            numero_nota = numero_nota.text
        else:
            # Se não encontrar, usa um nome padrão ou pula o elemento
            numero_nota = 'sem_numero'

        # Cria os elementos adicionais para ajustar estrutura tags do xml (ConsultarNfseResposta, ListaNfse, CompNfse).
        consultar_resposta = ET.Element('ConsultarNfseResposta', attrib={
                                        'xmlns': 'http://site.com.br'})
        lista_nfse = ET.SubElement(
            consultar_resposta, 'ListaNfse', attrib={'xmlns': ''})
        comp_nfse = ET.SubElement(lista_nfse, 'CompNfse')

        # Adiciona o elemento <Nfse> dentro de <CompNfse>
        comp_nfse.append(elem)

        # Cria uma nova árvore XML com os elementos adicionais
        # Cria uma nova árvore XML (new_tree).
        new_tree = ET.ElementTree(consultar_resposta)
        # Define o caminho do arquivo de saída (output_file).
        output_file = os.path.join(output_dir, f"{numero_nota}.xml")
        # Salva a nova árvore XML no arquivo de saída.
        new_tree.write(output_file, encoding='utf-8', xml_declaration=True)


# Define os caminhos do arquivo de entrada e do diretório de saída.
# Exemplo Caminho do arquivo XML de entrada.
file_path = 'C:\\Users\\Desktop\\XML\\00000.xml'
# Exemplo Diretório onde os arquivos XML divididos serão salvos.
output_dir = 'S:\\01_GERAL\\CONTABILIDADE TOPCOM\\NFs XML'
tag_name = './/Nfse'  # Nome da tag XML que será usada para dividir o arquivo.

# Execução. Chama a função split_xml com esses parâmetros para dividir o arquivo XML de entrada e salvar os arquivos divididos no diretório de saída.
split_xml(file_path, output_dir, tag_name)
