#!/usr/bin/env python3

import boto3

import argparse

labelFileName = "IMG_2324.JPG"
celebrityFileName = "killing-eve-poster.jpg"


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

  def imageCelebrity(self,imageFile):
  # https://docs.aws.amazon.com/rekognition/latest/dg/celebrities-procedure-image.html    
    with open(imageFile, 'rb') as image:
      response = self.client.recognize_celebrities(Image={'Bytes': image.read()})

    print('Detected faces for ' + imageFile)    
    for celebrity in response['CelebrityFaces']:
      print ('Name: ' + celebrity['Name'])
      print ('Id: ' + celebrity['Id'])
      print ('Position:')
      print ('   Left: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Height']))
      print ('   Top: ' + '{:.2f}'.format(celebrity['Face']['BoundingBox']['Top']))
      print ('Info')
      for url in celebrity['Urls']:
        print ('   ' + url)
      print

  def imageText(self,imageFile):
  # https://docs.aws.amazon.com/rekognition/latest/dg/text-detecting-text-procedure.html
    with open(imageFile, 'rb') as image:
      response = self.client.detect_text(Image={'Bytes': image.read()})
 
    textDetections=response['TextDetections']
    print ('Detected text')
    for text in textDetections:
            print ('Detected text:' + text['DetectedText'])
            print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print ('Parent Id: {}'.format(text['ParentId']))
            print ('Type:' + text['Type'])
            print

def handlerLabel(args):

    rekog = rekognition()
    rekog.imageLabels(labelFileName)
 
def handlerCelebrity(args):

    rekog = rekognition()
    rekog.imageCelebrity(celebrityFileName)

def handlerText(args):
    rekog = rekognition()
    rekog.imageText(celebrityFileName)

def main():

    #labelFileName = "IMG_2324.JPG"
    #celebrityFileName = "killing-eve-poster.jpg"

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser_name")

    detectLabels = subparsers.add_parser("label", help="Detect labels from image.")
    celebrityImage = subparsers.add_parser("celebrity", help="Recognize celebrities from image.")
    textImage = subparsers.add_parser("text", help="Detect text from image.")
    
    # https://stackoverflow.com/questions/8724262/argparse-why-the-code-is-executed-without-being-called
    # https://codereview.stackexchange.com/questions/93301/argparse-with-subparsers
    detectLabels.set_defaults(func = handlerLabel)
    celebrityImage.set_defaults(func = handlerCelebrity)
    textImage.set_defaults(func = handlerText)
   
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
   main()
