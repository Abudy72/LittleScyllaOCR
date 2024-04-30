from enum import Enum


class FileOutputProcessor:
    class FileOutputType(Enum):
        CSV = 'CSV'
        JSON = 'JSON'
        XML = 'XML'
        XLSX = 'XLSX'
        TEXT = 'TEXT'
        CONSOLE_LOG = 'CONSOLE_LOG'

    def __init__(self, filename, sanitized_text, file_output_type):
        self.filename = filename
        self.fileOutputType = file_output_type
        self.playerArray = sanitized_text.split

    def convert_text_to_players(self):
        # TODO convert sanitized_text to an array, here is where we verify the data
        return

    def produce_csv_file(self):
        def write_csv_file(input_test):
            return input_test.replace(' ', ',')

        with open('{}.csv'.format(self.filename), 'w') as file:
            file.write(write_csv_file(self.sanitizedText))

    def produce_xlsx_file(self):
        # TODO this method will produce
        return
