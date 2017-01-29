import os.path
import tempfile
import shutil
import datetime
from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.OperatingSystem import OperatingSystem
from resources.Variables import *


class Listener(object):

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, filename='robot_listens.txt'):
        super(Listener, self).__init__()
        outpath = os.path.join(tempfile.gettempdir(), filename)
        print('Listener log location: %s' + outpath)
        self.outfile = open(outpath, 'w')
        self.builtin = BuiltIn()

    def start_suite(self, name, attrs):
        self.suite_name = attrs['longname']
        self.output_dir = self.builtin.get_variable_value('${OUTPUT DIR}')
        # if results archiving is enabled, screenshots have already been moved
        # to the archive folder cleaning them now from the output folder
        if ARCHIVE_RESULTS:
            OperatingSystem().remove_files(self.output_dir +
                                           os.path.sep + '*.png')
        self.outfile.write("%s '%s'\n" % (name, str(attrs)))

    def start_test(self, name, attrs):
        self.outfile.write("%s '%s'\n" % (name, str(attrs)))

    def report_file(self, path):
        self.outfile.write("Finished writing to report file '%s'\n" % path)
        self.outfile.write("Path '%s'\n" % os.path.dirname(path))
        results_folder = os.path.dirname(path)
        shutil.make_archive('log', 'zip', results_folder)
        # if archiving is enabled, archive results
        if ARCHIVE_RESULTS:
            now = datetime.datetime.strftime(datetime.datetime.now(),
                                             '%Y%m%d%H%M%S')
            source_mask = self.output_dir + os.path.sep + '*.*'
            archive_run_dir = '{0}{1}{2}_{3}{1}'.format(
                ARCHIVE_DIR,
                os.path.sep,
                self._normalize_string(self.suite_name),
                now
            )
            OperatingSystem().copy_files(source_mask, archive_run_dir)

    @staticmethod
    def _normalize_string(value):
        return value.lower().replace(' ', '_')
