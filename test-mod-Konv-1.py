
import pandas as pd


class KONVERTOR:
     def __init__(self):
          self.DataIN = pd.DataFrame()
          self.DataOUT = pd.DataFrame()

     def set_DataIn(self, data: pd.DataFrame):
          # set input data
          self.DataIN = data.copy()
          return

     def get_DataOut(self):
          return self.DataOUT

     def konverze(self):
          # This method should contain the logic to convert DataIN to DataOUT
          # For now, we will just copy DataIN to DataOUT as a placeholder
          self.DataOUT = self.DataIN.copy()
          return
