import os;
import gzip;
def unzip(source_filename, dest_dir):
    with gzip.GzipFile(source_filename) as zf:
        for member in zf.infolist():
            extract_allowed = True;
            path = dest_dir;
            words = member.filename.split('/');
            for word in words:
                if (word == '..'):
                    extract_allowed = False;
                    break;
            if (extract_allowed == True):
                zf.decompress(member);
def unzipFiles(dest_dir):
    for file in os.listdir(dest_dir):
        print 'filename is %s' %file;
        if (os.path.isdir(dest_dir + '/' + file)):
            print '23';
            return unzipFiles(dest_dir + '/' + file);
        if file.endswith(".gz"):
            print 'Found file: "' + file + '" in "' + dest_dir + '" - extracting';
            unzip(dest_dir + '/' + file, dest_dir + '/');
unzipFiles('./GDS1038');
