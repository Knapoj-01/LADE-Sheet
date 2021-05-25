from pylatex import Document, Section, Subsection, Math, Matrix, NewLine
from pylatex.utils import italic, NoEscape
import numpy as np
def fill_document(doc):
    with doc.create(Section('ทดสอบภาษาไทย')):

        with doc.create(Subsection('หาอินเวิร์สและดีเทอร์มิแนนต์ของเมทริกซ์')):
            doc.append(NoEscape('\prob กำหนดให้'))
            matA = np.array([[1,2,3], [4,2,6], [7,5,9]])
            M = Matrix(matA,mtype='b')
            doc.append(Math(data=["A = ", M]))
            doc.append("จงหาอินเวิร์ส และดีเทอร์มิแนนต์ของเมทริกซ์นี้")
            doc.append(NewLine())
            doc.append(NoEscape('\sol'))          
            M = Matrix(np.round(np.linalg.inv(matA), 3),mtype='b')
            doc.append(Math(data=[NoEscape("A^{-1} = "), M]))




if __name__ == '__main__':
    # Basic document
    doc = Document('basic', fontenc= None, \
        inputenc= None, documentclass="subfiles",\
        document_options="../main.tex", lmodern=False,\
        textcomp=False, microtype=False)
    fill_document(doc)
    doc.generate_tex()
    doc.generate_pdf(compiler="xelatex")
  

    