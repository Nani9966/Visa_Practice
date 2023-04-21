from collections import namedtuple

DataIngestionArtifact = namedtuple("DataIngestedArtifact", ["train_file_path", "test_file_path","is_ingested","message"])

