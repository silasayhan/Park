



import unittest
import pandas as pd
import numpy as np
from predict_density import calculate_weekly_occupancy, train_regression_model, predict_density
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Örnek veri seti oluşturma (gerçek verilerinizi kullanmalısınız)
# Her bir gün için doluluk oranı (0 ile 1 arasında)
data = {
    'date': pd.date_range(start='2025-03-01', end='2025-03-15', freq='D'),
    'occupancy_rate': np.random.uniform(0.5, 1.0, 15)  # Örnek doluluk oranları
}

df = pd.DataFrame(data)

# Haftalık veriler için ortalama doluluk oranı
df['week'] = df['date'].dt.isocalendar().week
weekly_occupancy = df.groupby('week')['occupancy_rate'].mean()

# Günlük ve haftalık yoğunluk tahminleri için basit bir doğrusal regresyon modeli
# X: haftalık ortalama doluluk oranları, Y: yoğunluk
X = np.array(weekly_occupancy).reshape(-1, 1)
y = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300])  # Yoğunluk (örnek)

# Modeli oluşturma ve eğitme
model = LinearRegression()
model.fit(X, y)

# Yeni bir haftalık ortalama doluluk oranı verisi için tahmin yapma
new_weekly_rate = np.array([[0.85]])  # Örnek yeni doluluk oranı
predicted_density = model.predict(new_weekly_rate)

print(f'Tahmin edilen yoğunluk: {predicted_density[0]}')

# Doluluk oranı ile yoğunluk arasındaki ilişkiyi görselleştirme
plt.scatter(X, y, color='blue', label='Gerçek Yoğunluk')
plt.plot(X, model.predict(X), color='red', label='Tahmin Edilen Yoğunluk')
plt.xlabel('Haftalık Ortalama Doluluk Oranı')
plt.ylabel('Yoğunluk')
plt.legend()
plt.title('Doluluk Oranı ve Yoğunluk İlişkisi')
plt.show()



class TestPredictDensity(unittest.TestCase):

    def setUp(self):
        """Testlerden önce çalışacak fonksiyon."""
        # Örnek günlük veri
        self.data = {
            'date': pd.date_range(start='2025-03-01', end='2025-03-15', freq='D'),
            'occupancy_rate': np.random.uniform(0.5, 1.0, 15)  # Örnek doluluk oranları
        }
        self.df = pd.DataFrame(self.data)
        self.weekly_occupancy = calculate_weekly_occupancy(self.df)
        # Yoğunluk verisi (örnek)
        self.y = np.array([100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300])
        self.model = train_regression_model(self.weekly_occupancy, self.y)

    def test_calculate_weekly_occupancy(self):
        """Haftalık ortalama doluluk oranı hesaplamasını test etme."""
        weekly_occupancy = calculate_weekly_occupancy(self.df)
        self.assertEqual(len(weekly_occupancy), 2, "Haftalık doluluk oranı hatalı.")
        self.assertTrue(all(weekly_occupancy >= 0), "Haftalık doluluk oranı negatif olamaz.")

    def test_train_regression_model(self):
        """Regresyon modelinin düzgün çalışıp çalışmadığını test etme."""
        self.assertIsInstance(self.model, LinearRegression, "Model düzgün eğitilmemiş.")
    
    def test_predict_density(self):
        """Yoğunluk tahmininin doğruluğunu test etme."""
        new_weekly_rate = 0.85  # Yeni bir doluluk oranı
        predicted_density = predict_density(self.model, [new_weekly_rate])
        self.assertTrue(isinstance(predicted_density, float), "Tahmin edilen yoğunluk float olmalı.")
        self.assertGreater(predicted_density, 0, "Yoğunluk negatif olmamalı.")

if _name_ == "_main_":
    unittest.main()