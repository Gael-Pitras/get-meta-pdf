import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView

import PyPDF2

def get_pdf_version(pdf_file):
    with open(pdf_file, 'rb') as f:
        # Lire les 20 premiers octets pour chercher la version du PDF
        header = f.read(20).decode('latin1')
        version = ''
        if header.startswith('%PDF-'):
            version = header[5:8]  # Prendre la partie qui représente la version
    return version

def check_pdf_properties(pdf_file):
    pdf_version = get_pdf_version(pdf_file)
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        document_properties = pdf_reader.metadata
        creat_date = ''
        edit_date = ''
        creator = ''
        if document_properties:
            try:
                if document_properties.creation_date:
                    creat_date = str(document_properties.creation_date.strftime('%Y-%m-%d %H:%M:%S'))
                if document_properties.modification_date:
                    edit_date = str(document_properties.modification_date.strftime('%Y-%m-%d %H:%M:%S'))
                creator = document_properties.creator
            except ValueError:
                creat_date = ''
                edit_date = ''
        return {"creator": creator, "creat_date": creat_date, "edit_date": edit_date, "pdf_version": pdf_version}








def check_pdf_metadata(pdf_file):
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        document_properties = pdf_reader.metadata
        # print("Titre du document :", document_properties.title)
        # print("Auteur du document :", document_properties.author)
        # print("Auteur du document bis :", document_properties.author_raw)
        # print("Provenance :", document_properties.producer)
        # print("Subject :", document_properties.subject)
        # print("Xmp_metadata :", document_properties.xmp_metadata)
        if document_properties:
            return {"title": document_properties.title, "autor": document_properties.author, "provided": document_properties.producer, "subject":document_properties.subject, "xmp": document_properties.xmp_metadata}
        else:
            return {"title": "", "autor": "", "provided": "", "subject":"", "xmp": ""}
class PdfMetadataWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    
    def init_ui(self):
        # Créer les éléments de l'interface graphique
        self.file_label = QLabel('Fichier PDF:', self)
        self.file_edit = QLineEdit(self)
        self.browse_button = QPushButton('Parcourir', self)
        self.browse_button.clicked.connect(self.select_file)
        self.metadata_table = QTableWidget(self)
        self.metadata_table.setColumnCount(2)
        self.metadata_table.setHorizontalHeaderLabels(['Propriété', 'Valeur'])
        self.metadata_table.horizontalHeader().setStretchLastSection(True) # Étirer la dernière colonne pour remplir l'espace restant
        self.get_metadata_button = QPushButton('Obtenir les métadonnées', self)
        self.get_metadata_button.clicked.connect(self.get_metadata)

        # Créer un layout vertical pour contenir les éléments de l'interface graphique
        main_layout = QVBoxLayout(self)

        # Créer un layout horizontal pour contenir les éléments liés à la sélection de fichier
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_label)
        file_layout.addWidget(self.file_edit)
        file_layout.addWidget(self.browse_button)
        main_layout.addLayout(file_layout)

        # Ajouter le tableau de métadonnées au layout principal
        main_layout.addWidget(self.metadata_table)

        # Ajouter le bouton "Obtenir les métadonnées" au layout principal
        main_layout.addWidget(self.get_metadata_button)

        # Configurer la fenêtre
        self.setGeometry(200, 200, 500, 300)
        self.setWindowTitle('Récupération de métadonnées PDF')

    def select_file(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier
        file_path, _ = QFileDialog.getOpenFileName(self, 'Sélectionner un fichier PDF', '.', 'Fichiers PDF (*.pdf)')
        self.file_edit.setText(file_path)

    def get_metadata(self):
        # Obtenir les métadonnées du fichier PDF
        pdf_path = self.file_edit.text()
        properties = check_pdf_properties(pdf_path)
        metadata = check_pdf_metadata(pdf_path)

        # Réinitialiser le contenu de la table des métadonnées
        self.metadata_table.clearContents()
        self.metadata_table.setRowCount(0)

        # Ajouter les propriétés et les métadonnées au tableau
        self.metadata_table.setRowCount(len(properties) + len(metadata))
        row_index = 0

        # Ajouter les propriétés
        for key, value in properties.items():
            self.metadata_table.setItem(row_index, 0, QTableWidgetItem(str(key)))
            self.metadata_table.setItem(row_index, 1, QTableWidgetItem(str(value)))
            row_index += 1

        # Ajouter les métadonnées
        for key, value in metadata.items():
            self.metadata_table.setItem(row_index, 0, QTableWidgetItem(str(key)))
            self.metadata_table.setItem(row_index, 1, QTableWidgetItem(str(value)))
            row_index += 1

        # Redimensionner les colonnes de la table pour qu'elles prennent 50% de la largeur de la fenêtre chacune
        table_width = self.metadata_table.viewport().width()
        self.metadata_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.metadata_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)
        self.metadata_table.setColumnWidth(0, int(table_width / 2))
        self.metadata_table.setColumnWidth(1, int(table_width / 2))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = PdfMetadataWidget()
    widget.show()
    sys.exit(app.exec_())