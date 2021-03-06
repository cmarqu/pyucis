'''
Created on Jan 5, 2020

@author: ballance
'''
from pyucis import ucis
from pyucis.xml.xml_writer import XmlWriter
from pyucis.xml import validate_ucis_xml
from pyucis.xml.xml_reader import XmlReader

class XmlFactory():
    
    @staticmethod
    def read(file_or_filename) -> ucis:
        """Reads the specified XML file and returns a UCIS representation"""
        
        # First, validate the incoming XML
        if type(file_or_filename) == str:
            fp = open(file_or_filename)
        else:
            fp = file_or_filename

        try:            
            validate_ucis_xml(fp)
        except:
            if type(file_or_filename) == str:
                fp.close()
            

        fp.seek(0)
        
        reader = XmlReader()
        
        try:
            ret = reader.read(fp)
        finally:
            if type(file_or_filename) == str:
                fp.close()

        return ret
        
    @staticmethod
    def write(db : ucis, file_or_filename):
        """Writes the specified database in XML format"""
        writer = XmlWriter()
        
        if type(file_or_filename) == str:
            fp = open(file_or_filename, "w")
        else:
            fp = file_or_filename
        
        writer.write(fp, db)
        
        if type(file_or_filename) == str:
            fp.close()
            
        pass