#!/usr/bin/env python3

import boto3

class rekognition:
  def __init__(self):

    self.client = boto3.client('rekognition',region_name='us-east-1')

  def imageLabels(self,imageFile):
  # https://docs.aws.amazon.com/rekognition/latest/dg/images-bytes.html
    with open(imageFile, 'rb') as image:
      response = self.client.detect_labels(Image={'Bytes': image.read()})
        
    print('Detected labels in ' + imageFile)    
    for label in response['Labels']:
      print (label['Name'] + ' : ' + str(label['Confidence']))

    print('Done...')

def main():
    fileName = "./IMG_2324.JPG"

    rekog = rekognition()
    rekog.imageLabels(fileName)


if __name__ == "__main__":
   main()
