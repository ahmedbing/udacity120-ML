def featureScaling(arr):
    min = arr[0]
    max = 0
    for num in arr:
        if(num < min):
            min = num
        if(num > max):
            max = num
    for idx , num in enumerate(arr):
        arr[idx] = (num-min)*1.0 / (max-min) 
    return arr

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print(featureScaling(data))

