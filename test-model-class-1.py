
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


DD = KONVERTOR()
# Example usage:
data = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})
DD.set_DataIn(data)
DD.konverze()
# Get the converted data
converted_data = DD.get_DataOut()

# Output the converted data
print("Converted Data:") 
print(converted_data)

