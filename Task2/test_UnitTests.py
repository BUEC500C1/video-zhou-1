import pytest
import textToImg

# Test img files will save in expected format and name or not
def test_Img():
  testImgName = ["img/BU1.png", "img/NEU2.png", "img/MIT3.png",
    "img/Harvard4.png", "img/MU5.png", "img/UW6.png",
    "img/UCLA10.png", "img/UCB100.png", "img/NYU999.png"]

  accName = ["BU", "NEU", "MIT", "Harvard", "MU", "UW", "UCLA", "UCB", "NYU"]
  numbArr = [1, 2, 3, 4, 5, 6, 10, 100, 999]

  
  for a, n, t in zip(accName, numbArr, testImgName):
    # "testWords" is not important
    assert textToImg.textToImg("testWords", a, n) == t



    
#if __name__ == "__main__":
#  test_Img() 
