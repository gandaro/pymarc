r'''

The pymarc module provides an API for reading, writing and modifying
MARC records. MARC (MAchine Readable Cataloging) is a metadata format for
bibliographic data. More about MARC can be found at the Library of Congress:
http://lcweb.loc.gov/marc

Below are some common examples of how you might want to use pymarc. If you
run across an example that you think should be here please contribute it
by writing to the author.

1. Reading a batch of records and printing out the 245 subfield a. If you
   are curious this example uses the batch file available in the distribution.

    >>> from pymarc import MARCReader
    >>> reader = MARCReader(open('test/marc.dat', 'rb'))
    >>> for record in reader:
    ...    print record['245']['a']
    The pragmatic programmer :
    Programming Python /
    Learning Python /
    Python cookbook /
    Python programming for the absolute beginner /
    Web programming :
    Python programming on Win32 /
    Python programming :
    Python Web programming /
    Core python programming /
    Python and Tkinter programming /
    Game programming with Python, Lua, and Ruby /
    Python programming patterns /
    Python programming with the Java class libraries :
    Learn to program using Python :
    Programming with Python /
    BSD Sockets programming from a multi-language perspective /
    Design patterns :
    Introduction to algorithms /
    ANSI Common Lisp /

2. Creating a record and writing it out to a file.

    >>> from pymarc import Record, Field
    >>> record = Record()
    >>> record.addField(
    ...     Field(
    ...         tag = '245',
    ...         indicators = ['0','1'],
    ...         subfields = [
    ...             'a', 'The pragmatic programmer : ',
    ...             'b', 'from journeyman to master /',
    ...             'c', 'Andrew Hunt, David Thomas.'
    ...         ]))
    >>> out = open('file.dat', 'wb')
    >>> out.write(record.asMARC21())
    >>> out.close()

'''

from .record import Record, map_marc8_record
from .field import Field, RawField, map_marc8_field
from .exceptions import PymarcException, RecordLengthInvalid, \
    RecordLeaderInvalid, RecordDirectoryInvalid, NoFieldsFound, \
    BaseAddressInvalid, BaseAddressNotFound, WriteNeedsRecord, \
    NoActiveFile, FieldNotFound
from .reader import Reader, MARCReader, JSONReader, map_records
from .writer import Writer, JSONWriter, MARCWriter, TextWriter, XMLWriter
from .constants import LEADER_LEN, DIRECTORY_ENTRY_LEN, SUBFIELD_INDICATOR, \
    END_OF_FIELD, END_OF_RECORD
from .marc8 import marc8_to_unicode, MARC8ToUnicode
from .marcxml import XmlHandler, parse_xml, map_xml, parse_xml_to_array, \
    record_to_xml, record_to_xml_node
