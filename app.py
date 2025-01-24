class Studen(object):
  studen_count = 0

  def __new__(self):
    print('Studen.__new__')

  def __init__(self):
    print('Studen.__init__')
    self.gpa = 4.00

  def study_hard(self):
    print('Str, yes sir.')
