import requests
# Get product Id from user
productId = input("Enter a valid Product Id: \n")
if productId == '' or productId.isspace():
  print('Please enter a valid Product Id.')
else:
  try:
    URL = "https://dev.shopalyst.com/shopalyst-service/v1/products/" + productId
    # API call
    response = requests.get(url = URL, timeout = 5.0)
    data = response.json()
    attributeValues = data['attributeValues']
    skuSet = data['skuSet']

    # Function to get title and shade
    def getTitleAndShade(data):
      for attribute in attributeValues:
        if data == attribute['value']:
          title = attribute['title']
          shade = attribute['value']
          return title, shade

    # Formatting output data
    for idx, sku in enumerate(skuSet):
      title, shade = getTitleAndShade(sku['attributes']["1"])
      print(
      "------------",
      "Product: {}".format(idx + 1),
      "skuId: {}".format(sku['skuId']),
      "shade: {}".format(shade),
      "offerPrice: {}".format(sku['offerPrice']),
      "title: {}".format(title), sep='\n')
      print('\n')
  except requests.exceptions.Timeout as e:
    raise SystemExit(e)
  except requests.exceptions.RequestException as e:
    raise SystemExit(e)
