1. Memuat citra menggunakan OpenCV dengan fungsi cv2.imread().
2.Mengubah citra menjadi grayscale dengan fungsi cv2.cvtColor().
3.Menerapkan blur pada citra untuk mengurangi noise dengan fungsi cv2.GaussianBlur().
4.Menerapkan threshold pada citra untuk membuat citra biner dengan fungsi cv2.threshold().
5.Mencari kontur pada citra biner dengan fungsi cv2.findContours().
6.Melakukan loop pada setiap kontur yang ditemukan.
7.Mengabaikan kontur yang kecil dengan memeriksa luasnya.
8.Membuat mask untuk kontur dengan fungsi cv2.drawContours().
9.Menghitung rata-rata warna piksel di dalam mask dengan fungsi cv2.mean().
10.Mencari piksel serupa pada citra dengan menggunakan fungsi cv2.matchTemplate().
11.Menggambar persegi panjang di sekitar daerah yang cocok dengan fungsi cv2.rectangle().
12.Menampilkan hasil deteksi dengan fungsi cv2.imshow() dan cv2.waitKey().