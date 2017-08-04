import Blob
import itertools
import numpy as np

class blobs_manager:

    def __init__(self,blobs):

        if blobs is None:
            self.all_blobs = []
        else:
            self.all_blobs = blobs

    def add_blob(self,blob):
        self.all_blobs.append(blob)


    def delete_blobs(self,blobs):

        blob_set = set(blobs)
        blobs = list(blob_set)
        for blob in blobs:
            try:
                self.all_blobs.remove(blob)
            except ValueError:
                pass
            except IndexError:
                pass
    def replace_blob(self,index,blob):

        try:
            self.all_blobs[index] = blob
        except IndexError:
            pass


    def check_clash(self):
        blobs_to_delete = []
        for i,blob in enumerate(self.all_blobs):
            for j,other_blob in enumerate(self.all_blobs[:i-1] + self.all_blobs[i+1:]):

                if np.linalg.norm(np.array([blob.x, blob.y]) - np.array([other_blob.x, other_blob.y])) < (blob.size + other_blob.size):

                    if blob.size > other_blob.size:
                        print 'absorbed1'
                        # blob.blob_grow(other_blob.size)
                        blob.blob_grow(3)
                        self.replace_blob(i,blob)
                        blobs_to_delete.append(other_blob)

                    elif blob.size < other_blob.size:
                        print 'absorbed2'
                        # other_blob.blob_grow(blob.size)
                        other_blob.blob_grow(3)
                        self.replace_blob(j, other_blob)
                        blobs_to_delete.append(blob)

        self.delete_blobs(blobs_to_delete)

    def get_blobs(self):
        return self.all_blobs

