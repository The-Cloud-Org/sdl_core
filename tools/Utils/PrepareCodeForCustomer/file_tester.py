#!/usr/bin/env python
# -*- coding: utf-8 -*-

import customer_prepare
import os

class FilesTester:
#  Class to test Remover with real files
#  parce folder for testfiles
#  inputfiles mus be named like that: input_TestName
#  Expected result files: TestName.CUSTOMER.Result
#  $Result can be: Success, ParceFail, LengthFail, MatchFail
  input_mask = "input"
  results_dir = "results/"
  def __init__(self, foldername):
    files = os.listdir(foldername)
    input_files = []
    i = 0
    while (i < len(files)):
      f = files[i]
      if (f.find(self.input_mask) == 0): #file begins from "input" : input*
        input_files.append(f)
        files.remove(f)
      else:
        i += 1
    pairs = []
    i = 0
    print input_files
    for input_file in input_files:
      arr = input_file.split(".")
      test_name = arr[1]
      for test_file_name in files:
        pos = test_file_name.find(test_name) 
        if (pos != -1):
          arr = test_file_name.split(".")
          if ((len(arr) != 3) or (arr[0] != test_name)):
            print "Test files namiing error"
            continue
          customer_name =arr[1].upper()
          expected_result = arr[2]
          pairs.append((foldername + "/" + input_file, foldername + "/" + test_file_name, customer_name, test_name, expected_result))
    self.pairs = pairs
    for p in pairs:
      print p

  def run(self):
#	Run All tests
    for input_file_name, expected_result_file_name, customer_name, test_name, expected_result in self.pairs:
      print 80 * "="
      print test_name, "|", customer_name
      result = self.test(input_file_name,expected_result_file_name,customer_name, test_name)
      if (expected_result == result):
        print "SUCCESS"
      else:
        print "FAIL"
        print "\t expected: ", expected_result
        print "\t got: ", result
        
      print 80 * "="
      
  def test(self, input_file_name, expected_result_file_name, customer_name, test_name):
#	Run one test and return relust
    input_file = open(input_file_name, "rb")
    inp_lines = input_file.readlines()
    input_file.close()
    expected_result_file = open(expected_result_file_name, "rb")
    expected_lines = expected_result_file.readlines()
    expected_result_file.close()
    output = []
    result_code = ""
    warnings = ""
    try:
      output, warnings = customer_prepare.get_parsed_lines(inp_lines, customer_name)
    except customer_prepare.Error, ex:
      print input_file_name,": Error parsing file: ", ex;
      result_code = "ParceFail"
      
    if (len(output) != len(expected_lines)):
      print input_file_name,customer_name, ": Length does not matches: ", len(output), " != ", len(expected_lines)
      result_code += "LengthFail"
    else:
      length = len(output)
      i = 0
      while (i < length):
        result_line = output[i]
        expected_line = expected_lines[i]
        if (result_line != expected_line):
          print input_file_name, customer_name, "Match fail line ", i
          print "\t\t result_line :", result_line[:-1]
          print "\t\t expected_line :", expected_line[:-1]
          result_code += "MatchFail"
          break
        i += 1
    self.write_output(inp_lines, expected_lines, output, customer_name, test_name)
    if (len(result_code) == 0):
      return "Success"
    else:
      return result_code
    
  def write_output(self, origin_lines, expected_lines, result_lines, customer_name, test_name):
#	Write changed by Remover files to FS in result/ filder 
    f = open(self.results_dir + "origin_"+test_name + customer_name, "wb")
    for l in origin_lines:
      f.write(l)
    f.close()
    f = open(self.results_dir + "expected_"+test_name + customer_name, "wb")
    for l in expected_lines:
      f.write(l)
    f.close()   
    f = open(self.results_dir + "result_"+test_name + customer_name, "wb")
    for l in result_lines:
      f.write(l)
    f.close()   
    
def main():
  t = FilesTester("tests")
  t.run()
  return 0

if __name__ == '__main__':
  main()
