# matploit kütüphanesi
# görselleştirme kütüphanesi
# line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd 

df = pd.read_csv("Iris.csv")  # iris.csv dosyası okunup df ye atanıyor.

print("\nSpecies sütununda  kaç farklı değer var:")
print(df.Species.unique()) # tür sütununda kaç farklı değer var görmek için

print("\nIRIS Sütun isimleri:")
print(df.columns) # sütunlara bakıyoruz


print("\nDatafame hakkında bilgi:")
print(df.info()) # dataframe hakkında genel bilgi edinmek için 
print(df.describe()) # dataframe hakkında genel bilgi edinmek için 


setosa = df[df.Species == "Iris-setosa"] # setosaları içeren df
versicolor = df[df.Species == "Iris-versicolor"] # versicolorları içeren df
virginica = df[df.Species == "Iris-virginica"] # virginicaları içeren df


# datalarla karşılaştırma yapıp bilgi sahibi olmak için 
print("\nHer türdeki datalar hakkında karşılaştırma yapmak için ayrı ayrı bilgileri:")
print("\nIris-setosa".upper())
print(setosa.describe())
print("\nIris-versicolor".upper())
print(versicolor.describe())
print("\nIris-virginica".upper())
print(virginica.describe())

import matplotlib.pyplot as plt

df1 = df.drop(["Id"], axis = 1) # ihtiyaç olmadığı için id yi sildik

###Line Plot

df1.plot(grid = True, alpha = 0.5) # linestyle = ":" ->noktalı # görselleştirme için bir yöntem default line plot
plt.title("Line Plot - Genel")
plt.show()

# görselleştirme için değerleri ayarlıyoruz 
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = " setosa")
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = " versicolor")
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue", label = " virginica")
plt.title("Line Plot - PetalLengthCm") # Grafiğe başlık ekledik 
plt.xlabel("Id") # x değerinin adı
plt.ylabel("PetalLengthCm") # y değerinin adı
plt.legend() # en uygun yerlere yerleştir 
plt.show() # görselleştir.


### Scatter Plot 
# Genelde iki feature karşılaştırmak için kullanılır 
# scatter ile görselleştirme 

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm, color = "Red" , label = "Setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm, color = "Green" , label = "Versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm, color = "Blue" , label = "Virginica")
plt.legend() # en uygun yerlere yerleştir 
plt.xlabel("PetalLengthCm") # x değerinin adı
plt.ylabel("PetalWidthCm") # y değerinin adı
plt.title("Scatter Plot") # Grafiğe başlık ekledik 
plt.show() # görselleştir.

### Histogram 

plt.hist(setosa.PetalLengthCm , bins = 30)
plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("Hist")
plt.legend()
plt.show()

### Bar plot

plt.bar(setosa.Id, setosa.PetalLengthCm)
plt.title("Bar Plot")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.show()


### Subplots
# genel grafiği alt grafiklere parçalamak için 

df1.plot(grid = True, alpha = 0.5, subplots = True) # genel grafiği alt grafiklere parçalamak için 
plt.show()

# kendimizin parçaladığı subplots
plt.subplot(2, 1, 1) # 2 değer alacak 1 in  1. si
plt.plot(setosa.Id, setosa.PetalLengthCm, color = "red", label = "selosa")
plt.ylabel("setosa - PetalLengthCm")

plt.subplot(2, 1, 2) # 2 değer alacak 1 in  2. si
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green", label = "versicolor")
plt.ylabel("versicolor - PetalLengthCm")
plt.show()





