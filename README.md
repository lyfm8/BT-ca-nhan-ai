# 🧠 CÁC THUẬT TOÁN TÌM KIẾM TRONG AI

---

## I. Nhóm Thuật Toán Tìm Kiếm Không Có Thông Tin

---

### **1. Breadth-First Search (BFS)**

![demo-bfs](gif/bfs.gif)

#### **Lý thuyết**

- **Khái niệm:**  
  Tìm kiếm theo chiều rộng, duyệt từng mức của cây trạng thái từ gốc ra ngoài.

- **Cách hoạt động:**  
  1. Bắt đầu từ nút gốc, dùng hàng đợi để lưu các nút chờ mở rộng.  
  2. Lần lượt mở rộng tất cả nút ở độ sâu 0, rồi 1, rồi 2,... cho đến khi tìm được đích.

- **Ưu điểm:**  
  - Tìm được lời giải ngắn nhất nếu chi phí các bước đi bằng nhau.  
  - Đơn giản, trực quan.

- **Nhược điểm:**  
  - Tốn nhiều bộ nhớ khi không gian trạng thái lớn.

- **Độ phức tạp:**  
  - Thời gian: `O(b^d)`  
  - Bộ nhớ: `O(b^d)`  
  - Trong đó **b** là hệ số phân nhánh, **d** là độ sâu của lời giải.

#### **Ứng dụng trong game đặt 8 quân xe**

- Hàm `bfs_rooks()` thực hiện thuật toán tìm kiếm theo chiều rộng (BFS).

**Cách hoạt động:**

- Bắt đầu với hàng đợi chứa trạng thái rỗng `[]` (chưa đặt quân nào).  
- Mỗi vòng lặp: lấy một trạng thái ra khỏi hàng đợi, mở rộng nó bằng cách thêm 1 quân xe vào cột chưa dùng theo nguyên tắc **FIFO**.  
- Mỗi trạng thái con được thêm vào hàng đợi để tiếp tục mở rộng sau.  
- Khi trạng thái có đủ `n` quân xe (mỗi hàng một quân), thuật toán dừng và trả về nghiệm.  
- Nếu hàng đợi rỗng mà chưa tìm thấy nghiệm → kết thúc với thông báo thất bại.

---

### **2. Depth-First Search (DFS)**

![demo-dfs](gif/dfs.gif)

#### **Lý thuyết**

- **Khái niệm:**  
  Tìm kiếm theo chiều sâu, đi sâu vào một nhánh cho đến khi gặp đích hoặc bế tắc.

- **Cách hoạt động:**  
  - Dùng ngăn xếp (hoặc đệ quy) để theo dõi đường đi hiện tại.  
  - Mở rộng nút con đầu tiên liên tiếp; khi không thể mở rộng thì **quay lui (backtrack)** lên nút cha.

- **Ưu điểm:**  
  - Tốn ít bộ nhớ hơn BFS.  
  - Có thể tìm lời giải nhanh khi nó nằm sâu nhưng ở nhánh đầu.

- **Nhược điểm:**  
  - Không đảm bảo tìm lời giải tối ưu.  
  - Có thể rơi vào vòng lặp nếu không kiểm soát.

- **Độ phức tạp:**  
  - Thời gian: `O(b^m)`  
  - Bộ nhớ: `O(b * m)`  
  - Trong đó **b** là hệ số phân nhánh, **m** là độ sâu tối đa của cây.

#### **Ứng dụng trong game đặt 8 quân xe**

- Hàm `dfs_rooks()` thực hiện thuật toán tìm kiếm theo chiều sâu (DFS).

**Cách hoạt động:**

- Khởi tạo ngăn xếp chứa trạng thái rỗng `[]`.  
- Mỗi vòng lặp: lấy trạng thái ở đỉnh ngăn xếp ra (ưu tiên đi sâu nhất) theo nguyên tắc **LIFO**.  
- Nếu trạng thái có đủ `n` quân xe → trả về nghiệm.  
- Ngược lại, sinh các trạng thái con bằng cách thêm 1 quân xe vào cột chưa được dùng và đẩy chúng vào ngăn xếp.  
- Tiếp tục cho đến khi ngăn xếp rỗng → không tìm thấy nghiệm hợp lệ.

---

### **3. Uniform Cost Search (UCS)**

![demo-ucs](gif/ucs.gif)

#### **Lý thuyết**

- **Khái niệm:**  
  Tìm kiếm theo chi phí, luôn mở rộng nút có chi phí đường đi `g(n)` nhỏ nhất trước.

- **Cách hoạt động:**  
  - Dùng **hàng đợi ưu tiên (priority queue)** sắp theo `g(n)`.  
  - Khi pop một nút đích từ hàng đợi, đảm bảo đó là đường đi chi phí nhỏ nhất.

- **Ưu điểm:**  
  - Luôn tìm được nghiệm tối ưu nếu chi phí các bước là không âm.

- **Nhược điểm:**  
  - Có thể tốn thời gian/bộ nhớ lớn nếu không có heuristic.

- **Độ phức tạp:**  
  - Thời gian: `O(b^(1 + ⌊C*/ε⌋))`  
  - Bộ nhớ: `O(b^(1 + ⌊C*/ε⌋))`  
  - Trong đó **b** là hệ số phân nhánh, **C*** là chi phí của lời giải tối ưu, **ε** là kích thước bước chi phí nhỏ nhất.

#### **Ứng dụng trong game đặt 8 quân xe**

- Hàm `ucs_rooks()` hoạt động như sau:

  - Bắt đầu với hàng đợi ưu tiên chứa trạng thái rỗng `[]` có chi phí `0`.  
  - Mỗi vòng lặp: lấy ra trạng thái có cost nhỏ nhất trong hàng đợi để mở rộng.  
  - Nếu trạng thái có đủ `n` quân xe → trả về nghiệm cùng tổng chi phí.  
  - Ngược lại, sinh các trạng thái con bằng cách thêm 1 quân xe vào cột chưa dùng, tính chi phí mới qua `cost_function()` rồi đưa vào hàng đợi ưu tiên.  
  - Lặp lại cho đến khi tìm thấy nghiệm tối ưu hoặc hàng đợi rỗng.

---

### **4. Depth-Limited Search (DLS)**

![demo-dls](gif/dls.gif)

#### **Lý thuyết**

- **Khái niệm:**  
  Phiên bản của DFS với giới hạn độ sâu tối đa `L`.

- **Cách hoạt động:**  
  - Thực hiện DFS nhưng **không mở rộng** các nút có độ sâu vượt quá `L`.  
  - Nếu đến độ sâu `L` mà chưa tìm thấy đích thì trả về **failure** (hoặc **cut-off**).

- **Ưu điểm:**  
  - Tránh vòng lặp vô hạn khi không có kiểm tra visited.  
  - Kiểm soát bộ nhớ.

- **Nhược điểm:**  
  - Có thể bỏ sót lời giải nếu nằm sâu hơn giới hạn `L`.

- **Độ phức tạp:**  
  - Thời gian: `O(b^L)`  
  - Bộ nhớ: `O(b * L)`  
  - Trong đó **b** là hệ số phân nhánh, **L** là độ sâu giới hạn.

#### **Ứng dụng trong game đặt 8 quân xe**

- Hàm `dls_rooks(limit=8)` hoạt động như sau:

  - Bắt đầu từ trạng thái rỗng `[]`, gọi hàm đệ quy `dls(state, depth)` để mở rộng dần từng mức.  
  - Ở mỗi bước:  
    - Nếu trạng thái đủ `n` quân xe → trả về nghiệm.  
    - Nếu đạt độ sâu giới hạn `limit` → dừng mở rộng và quay lui.  
    - Ngược lại, sinh các trạng thái con bằng cách thêm 1 quân xe vào cột chưa dùng rồi gọi đệ quy tăng độ sâu lên 1.  
  - Quá trình tiếp tục cho đến khi tìm được nghiệm hợp lệ hoặc toàn bộ nhánh đều bị cắt do đạt giới hạn độ sâu.

---

### **5. Iterative Deepening (ID)**

![demo-id](gif/id.gif)

#### **Lý thuyết**

- **Khái niệm:**  
  Kết hợp ưu điểm của BFS (tối ưu theo bước) và DFS (bộ nhớ thấp) bằng cách lặp DLS với `L` tăng dần từ 0 tới `d`.

- **Cách hoạt động:**  
  - Thực hiện DLS với `L = 0`, rồi `L = 1`, rồi `L = 2`, ... cho đến khi tìm thấy lời giải.  
  - Mỗi lần lặp giống một DFS nhưng giới hạn sâu khác nhau.

- **Ưu điểm:**  
  - Tìm được lời giải tối ưu như BFS.  
  - Chỉ dùng bộ nhớ như DFS.

- **Nhược điểm:**  
  - Lặp lại nhiều lần các node ở các mức nông (tốn CPU).

- **Độ phức tạp:**  
  - Thời gian: `O(b^d)`  
  - Bộ nhớ: `O(b * d)`  
  - Trong đó **b** là hệ số phân nhánh, **d** là độ sâu của lời giải.

#### **Ứng dụng trong game đặt 8 quân xe**

- Hàm `id_rooks()` là vòng điều khiển chính:

  - Bắt đầu từ giới hạn độ sâu `limit = 1`, tăng dần tới `n`.  
  - Mỗi lần lặp sẽ gọi `id_dfs_rooks(limit)` để tìm nghiệm ở giới hạn đó.  
  - Nếu tìm thấy nghiệm → thuật toán dừng và trả về kết quả.  
  - Nếu không → tiếp tục tăng giới hạn và thử lại.

- Hàm `id_dfs_rooks(limit)` là bước tìm kiếm theo chiều sâu có giới hạn:

  - Dùng **ngăn xếp (stack)** để duyệt theo DFS.  
  - Mỗi trạng thái là danh sách vị trí quân xe đã đặt.  
  - Khi đạt tới `limit`, thuật toán **quay lui (backtrack)**.  
  - Khi có đủ `n` quân, kiểm tra xem có khớp với trạng thái đích (`goal_cols`) bằng `check_goal_state()`.


## II. Nhóm Thuật Toán Tìm Kiếm Có Thông Tin

### 1. Greedy Best-First Search

![demo-greedy](gif/greedy.gif)

**Lý Thuyết:**
* **Khái niệm:** Chọn mở rộng nút có heuristic *h(n)* nhỏ nhất — tức là nút "có vẻ" gần đích nhất.  
* **Cách hoạt động:**
  - Dùng hàng đợi ưu tiên sắp theo *h(n)*.  
  - Luôn mở rộng nút có *h(n)* thấp nhất, không xét *g(n)* (chi phí đã đi).  
* **Ưu điểm:** Nhanh trong nhiều trường hợp vì tập trung theo heuristic.  
* **Nhược điểm:** Không đảm bảo nghiệm tối ưu, dễ rơi vào bẫy heuristic (local optimum).  
* **Độ phức tạp:**
  - Thời gian: O(b^d) (trường hợp xấu)  
  - Bộ nhớ: O(b^d)  
  - Trong đó *b* là hệ số phân nhánh, *d* là độ sâu của lời giải; hiệu năng thực tế phụ thuộc mạnh vào chất lượng hàm heuristic *h(n)*.

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `greedy_search_rooks()`:**
Thuật toán xây dựng nghiệm từng bước từ trên xuống dưới (theo từng hàng).

Ở mỗi bước (ứng với một hàng):
- Xét tất cả các cột còn trống và tính cost cho việc đặt quân ở cột đó.  
- Chọn cột có cost nhỏ nhất (được đánh giá tốt nhất theo `cost_function`).  
- Thêm vị trí được chọn vào trạng thái hiện tại (*state*) và loại bỏ cột đó khỏi danh sách cột còn lại.  
- Lặp lại cho đến khi tất cả các hàng đã được đặt quân.

---

### 2. A* Search

![demo-a_star](gif/a_star.gif)

**Lý Thuyết:**
* **Khái niệm:** Kết hợp giữa chi phí thực tế *g(n)* và heuristic *h(n)* bằng *f(n) = g(n) + h(n)* để chọn nút mở rộng.  
* **Cách hoạt động:**
  - Dùng hàng đợi ưu tiên sắp theo *f(n)*.  
  - Mở rộng nút có *f(n)* nhỏ nhất; với heuristic *admissible* (không đánh giá quá thấp) thì A* tìm lời giải tối ưu.  
* **Ưu điểm:** Đầy đủ và tối ưu nếu *h(n)* là admissible; nếu *h(n)* còn consistent thì cập nhật đơn giản hơn.  
* **Nhược điểm:** Tốn bộ nhớ vì phải lưu open/closed lists; có thể nổ bộ nhớ trên không gian lớn.  
* **Độ phức tạp:**
  - Thời gian: O(b^d) (trường hợp xấu; thực tế phụ thuộc chất lượng *h*)  
  - Bộ nhớ: O(b^d)  
  - Trong đó *b* là hệ số phân nhánh, *d* là độ sâu lời giải; hiệu năng cải thiện khi *h* càng gần giá trị thực.

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `a_star_search()`:**
Thuật toán sử dụng hàng đợi ưu tiên (priority queue) để mở rộng các trạng thái có giá trị *f = g + h* nhỏ nhất trước, trong đó:

- *g:* Chi phí thực tế từ trạng thái ban đầu đến trạng thái hiện tại.  
- *h:* Giá trị heuristic (ước lượng chi phí còn lại đến đích), tính bằng `cost_function`.  
- *f:* Tổng chi phí ước lượng (*f = g + h*).  

Ban đầu, thuật toán khởi tạo với trạng thái rỗng (`[]`) và *f = 0*.  

Ở mỗi vòng lặp:
- Lấy ra trạng thái có *f* nhỏ nhất trong hàng đợi.  
- Nếu trạng thái này có đủ *n* quân → nghiệm hoàn chỉnh.  
- Nếu chưa đủ → mở rộng các trạng thái con bằng cách thêm quân mới vào các cột còn trống.  
- Mỗi trạng thái con được tính lại *f, g, h* và thêm vào hàng đợi.  
- Các trạng thái đã được mở rộng được lưu vào tập *seen* để tránh lặp lại.

---

## III. Nhóm Thuật Toán Tìm Kiếm Cục Bộ

### 1. Hill Climbing

![demo-hc](gif/hc.gif)

**Lý Thuyết:**
* **Khái niệm:** Bắt đầu từ một trạng thái ban đầu, lặp tìm trạng thái lân cận tốt hơn theo hàm mục tiêu.  
* **Cách hoạt động:**
  - Từ trạng thái hiện tại, sinh tất cả (hoặc một số) trạng thái lân cận.  
  - Chọn trạng thái có giá trị tốt nhất; nếu không có trạng thái tốt hơn thì dừng (có thể local optimum).  
* **Ưu điểm:** Đơn giản, nhanh cho các bài toán có không gian lớn nhưng cục bộ mượt.  
* **Nhược điểm:** Dễ kẹt ở cực trị địa phương, plateaus, hoặc rơi local optimum.  
* **Độ phức tạp:**
  - Thời gian: O(i * b)  
  - Bộ nhớ: O(n)  
  - Trong đó *i* là số vòng lặp, *b* là số lân cận mỗi bước, *n* là kích thước trạng thái.

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `hill_climbing()`:**
- Khởi tạo ngẫu nhiên trạng thái ban đầu `state` (vị trí các quân xe).  
- Tính cost hiện tại (`cur_cost`) dựa trên `cost_function` — giá trị càng nhỏ càng tốt.  
- Trong mỗi vòng lặp:
  - Sinh ra tất cả các trạng thái lân cận (`get_neighbors`).  
  - Tính cost cho từng neighbor, chọn neighbor có cost nhỏ nhất.  
  - Nếu neighbor tốt hơn → cập nhật trạng thái.  
  - Nếu không có neighbor tốt hơn → dừng (local optimum).

---

### 2. Simulated Annealing

![demo-sa](gif/sa.gif)

**Lý Thuyết:**
* **Khái niệm:** Mở rộng hill climbing bằng cách chấp nhận các bước xấu với xác suất giảm dần (theo “nhiệt độ”) để thoát local optimum.  
* **Cách hoạt động:**
  - Ở mỗi bước, chọn ngẫu nhiên một trạng thái lân cận.  
  - Nếu tốt hơn → chấp nhận; nếu xấu hơn → chấp nhận với xác suất *e^{-Δ/T}*.  
  - Giảm *T* dần theo lịch (schedule).  
* **Ưu điểm:** Có thể thoát local optimum và tìm gần tới global optimum.  
* **Nhược điểm:** Cần tinh chỉnh lịch nhiệt độ; chậm nếu cần chất lượng tốt.  
* **Độ phức tạp:**
  - Thời gian: O(i * b)  
  - Bộ nhớ: O(n)

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `simulated_annealing()`:**
- Khởi tạo nhiệt độ *T*, nhiệt độ tối thiểu *T_min* và hệ số làm nguội *alpha*.  
- Sinh ngẫu nhiên trạng thái ban đầu `state`, tính cost hiện tại (`cur_cost`) bằng `heuristic_conflict`.  
- Trong mỗi vòng lặp:
  - Sinh neighbor mới bằng cách thay đổi ngẫu nhiên vị trí một quân.  
  - Tính Δ = new_cost - cur_cost.  
  - Nếu Δ ≤ 0 → chấp nhận ngay.  
  - Nếu Δ > 0 → chấp nhận với xác suất *P = e^{-Δ / T}*.  
  - Giảm nhiệt độ: *T *= alpha*.  
- Dừng khi *T < T_min* hoặc đạt điều kiện dừng.

---

### 3. Beam Search

![demo-beam](gif/beam.gif)

**Lý Thuyết:**
* **Khái niệm:** Giữ lại tối đa *k* trạng thái tốt nhất (beam width) ở mỗi bước, thay vì giữ toàn bộ frontier.  
* **Cách hoạt động:**
  - Từ *k* trạng thái hiện tại, sinh tất cả con.  
  - Chọn *k* trạng thái tốt nhất làm beam cho bước kế tiếp.  
* **Ưu điểm:** Tiết kiệm bộ nhớ hơn tìm kiếm toàn diện.  
* **Nhược điểm:** Không đảm bảo tìm lời giải tối ưu; nếu *k* nhỏ dễ bỏ nghiệm tốt.  
* **Độ phức tạp:**
  - Thời gian: O(k * b * d)  
  - Bộ nhớ: O(k * d)

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `beam_search()`:**
- Khởi tạo beam ban đầu gồm 1 trạng thái rỗng (0, []).  
- Với mỗi hàng:
  - Mở rộng tất cả trạng thái trong beam để sinh candidate mới.  
  - Tính cost bằng `cost_function`.  
  - Chọn ra *k* trạng thái có cost nhỏ nhất.  
- Khi hết hàng hoặc không còn candidate hợp lệ → chọn trạng thái tốt nhất trong beam làm kết quả.

---

### 4. Genetic Algorithm

![demo-ga](gif/ga.gif)

**Lý Thuyết:**
* **Khái niệm:** Thuật toán tiến hóa dùng quần thể các cá thể, áp dụng chọn lọc, lai ghép và đột biến để tiến đến nghiệm tốt.  
* **Cách hoạt động:**
  - Khởi tạo quần thể kích thước *P*.  
  - Lặp: đánh giá fitness, chọn cá thể, lai ghép, đột biến qua *G* thế hệ.  
* **Ưu điểm:** Mạnh với không gian tìm kiếm lớn và đa cực trị; dễ song song hóa.  
* **Nhược điểm:** Nhiều siêu tham số cần tinh chỉnh; không đảm bảo tối ưu toàn cục.  
* **Độ phức tạp:**
  - Thời gian: O(P * G * L)  
  - Bộ nhớ: O(P * L)

**Ứng Dụng Trong Game Đặt 8 Quân Xe — Hàm `genetic_algorithm()`:**
- **Khởi tạo quần thể ban đầu:**  
  - Tạo `population_size` cá thể, mỗi cá thể là chuỗi 8 gen (vị trí của 8 quân).  
  - Tính fitness bằng `heuristic_conflict()`.  
- **Tiến hóa qua từng thế hệ:**  
  - Nếu có cá thể đạt cost = 0 → dừng.  
  - **Chọn lọc:** Lấy 2 cá thể tốt nhất (bố và mẹ).  
  - **Lai ghép:** Tạo 2 con bằng cách ghép nửa đầu bố + nửa sau mẹ, rồi ngược lại.  
  - **Đột biến:** Xác suất 10%, thay đổi ngẫu nhiên một gen.  
  - **Cập nhật quần thể:** Giữ lại con tốt nhất, thêm cá thể ngẫu nhiên để đủ kích thước.  
- **Kết thúc:**  
  - Sau *max_generations*, chọn cá thể có cost thấp nhất làm kết quả.



## IV. Nhóm Thuật Toán Tìm Kiếm Theo Ràng Buộc

### 1. Backtracking + Forward Checking

![demo-bfc](gif/bfc.gif)

-- **Lý Thuyết**  
* **Khái Niệm:** thử gán giá trị cho biến theo thứ tự, quay lui khi mâu thuẫn, và dùng forward checking để loại bỏ giá trị không khả thi cho các biến còn lại.  
* **Cách Hoạt Động:**  
  - chọn biến chưa gán, thử từng giá trị hợp lệ, cập nhật miền (domain) các biến chưa gán bằng forward checking,  
  - nếu một biến có miền rỗng thì quay lui; tiếp tục đến khi gán đủ.  
* **Ưu Điểm:**  
  - giảm đáng kể không gian tìm kiếm so với brute force.  
* **Nhược Điểm:**  
  - vẫn có thể tốn thời gian nếu ràng buộc yếu hoặc thứ tự biến xấu.  
* **Độ Phức Tạp:**  
  - thời gian: `O(d^n)` trong trường xấu nhất  
  - trong đó n là số biến, d là kích thước miền giá trị trung bình.  

-- **Ứng Dụng Trong Game Đặt 8 Quân Xe - Hàm `backtracking_fc()`:**

**Khởi Tạo:**  
- Bắt đầu với hàng đầu tiên (`row = 0`) và miền giá trị ban đầu cho mỗi hàng là tất cả các cột khả thi `[[0, 1, ..., n-1], ...]`.  
- Gọi hàm đệ quy `forward_checking(0, [], initial_col)` để bắt đầu quá trình tìm kiếm.  

**Đệ Quy Forward Checking:**  
- Ở mỗi hàng `row`, thuật toán lần lượt thử đặt quân tại các cột khả thi trong `col_available[row]`.  
- Mỗi khi đặt một quân tại ô `(row, col)`, thuật toán sẽ cập nhật miền giá trị (domain) của các hàng sau bằng cách loại bỏ cột vừa chọn — đây chính là forward checking.  

**Kiểm Tra Miền Hợp Lệ:**  
- Sau khi loại bỏ, nếu bất kỳ hàng nào phía dưới không còn cột khả thi, nhánh hiện tại bị loại bỏ ngay (backtrack).  
- Nếu vẫn còn miền hợp lệ, thuật toán đệ quy sang hàng kế tiếp với miền giá trị đã được cập nhật.  

**Điều Kiện Dừng:**  
- Khi `row == n`, tức là đã đặt đủ n quân mà không xảy ra xung đột, thuật toán lưu nghiệm hợp lệ vào danh sách kết quả `solutions`.  

**Kết Thúc:**  
- Nếu tồn tại ít nhất một nghiệm → trả về nghiệm đầu tiên tìm được.  
- Nếu không có nghiệm nào hợp lệ → thông báo không tìm thấy lời giải.  

---

### 2. AC-3 (Arc Consistency 3)

![demo-ac3](gif/ac3.gif)

-- **Lý Thuyết**  
* **Khái Niệm:** thuật toán đạt tính khớp cung (arc consistency) cho các ràng buộc nhị phân, loại bỏ giá trị không còn khả thi.  
* **Cách Hoạt Động:**  
  - đưa tất cả cung `(Xi, Xj)` vào hàng đợi,  
  - lặp: lấy một cung, cô lập các giá trị không có đối ứng hợp lệ và cập nhật miền; nếu thay đổi thì thêm các cung liên quan vào hàng đợi.  
* **Ưu Điểm:**  
  - tiền xử lý tốt giúp backtracking hiệu quả hơn; giảm miền giá trị sớm.  
* **Độ Phức Tạp:**  
  - thời gian: `O(e * d^3)`  
  - trong đó e là số ràng buộc (số cung), d là kích thước miền giá trị lớn nhất.  

-- **Ứng Dụng Trong Game Đặt 8 Quân Xe - Hàm `ac3()`:**

**Khởi Tạo Miền Giá Trị:**  
- Gán cho mỗi biến (ứng với một hàng) một miền giá trị ban đầu `domain = {r: {0, 1, ..., n-1}}`.  
- Tạo hàng đợi tất cả các cung `(xi, xj)` với `xi ≠ xj`, biểu diễn ràng buộc giữa các biến.  

**Duy Trì Tính Nhất Quán Cung (Arc Consistency):**  
- Lấy một cung `(xi, xj)` ra và gọi hàm `revise()` để kiểm tra xem có giá trị nào trong `domain[xi]` không còn phù hợp với mọi giá trị của `xj` không.  
- Nếu có, loại bỏ những giá trị đó khỏi `domain[xi]`.  
- Nếu `domain[xi]` trở nên rỗng, thuật toán kết luận thất bại (không có nghiệm).  
- Nếu `domain[xi]` bị thay đổi, thêm lại các cung `(xk, xi)` (với `xk ≠ xi, xk ≠ xj`) vào hàng đợi để duy trì tính nhất quán lan truyền.  

**Kết Quả Sau Khi Duy Trì Nhất Quán:**  
- Khi hàng đợi rỗng, nghĩa là tất cả các miền đã nhất quán cung — tức mọi giá trị còn lại trong mỗi `domain[xi]` đều hợp lệ với các biến khác.  
- Thuật toán ghi lại miền giá trị sau khi ràng buộc.  

**Giai Đoạn Backtracking Sau AC-3:**  
- Dùng backtracking để chọn cụ thể một giá trị cho mỗi biến sao cho không trùng cột.  
- Với mỗi hàng `r`, thử lần lượt các giá trị trong `domain[r]`.  
- Nếu chọn được cột chưa dùng, đặt quân và tiếp tục sang hàng kế tiếp.  
- Nếu không còn giá trị hợp lệ, quay lui để thử giá trị khác.  

**Điều Kiện Dừng Và Kết Quả:**  
- Nếu đã chọn được giá trị cho tất cả các hàng → tìm thấy nghiệm hợp lệ.  
- Nếu không tìm được giá trị nào phù hợp → không có lời giải.  

---

## V. Nhóm Thuật Toán Tìm Kiếm Phân Rã

### 1. And-Or Search

![demo-ao](gif/ao.gif)

-- **Lý Thuyết**  
* **Khái Niệm:** mô hình cây gồm nút **OR** (chọn một hành động) và nút **AND** (phải giải quyết toàn bộ các nhánh con), phù hợp cho lập kế hoạch phân rã hoặc bài toán có cấu trúc con.  
* **Cách Hoạt Động:**  
  - mở rộng theo kiểu **AND/OR**: với nút **OR** thử từng hành động (một trong các lựa chọn), với nút **AND** phải kết hợp nghiệm từ tất cả nhánh con,  
  - dùng đệ quy và memoization để tránh lặp lại.  
* **Độ Phức Tạp:**  
  - thời gian: số mũ theo kích thước phân rã (exponential)  
  - phụ thuộc số lượng nhánh tại nút OR/AND và độ sâu phân rã.  

-- **Ứng Dụng Trong Game Đặt 8 Quân Xe - Hàm `and_or_search()`:**

**Khởi Tạo:**  
- Thuật toán bắt đầu từ trạng thái rỗng (chưa đặt quân nào) và gọi hàm `or_search([], [])`.  
- Mục tiêu là tìm một kế hoạch (plan) — tức chuỗi hành động — dẫn tới trạng thái đích (goal).  

**Hàm OR-SEARCH:**  
- Đại diện cho một nút **OR** — ta có nhiều lựa chọn hành động có thể thực hiện.  
- Với mỗi hành động khả thi (ví dụ: chọn một cột để đặt quân ở hàng hiện tại), thuật toán sẽ:  
  - sinh ra trạng thái mới bằng `results(state, action)`,  
  - gọi `and_search(...)` để kiểm tra xem tất cả hệ quả của hành động đó có thể dẫn tới goal không.  
- Nếu ít nhất một hành động dẫn đến thành công → trả về kế hoạch tương ứng.  
- Nếu không hành động nào thành công → trả về `None`.  

**Hàm AND-SEARCH:**  
- Đại diện cho một nút **AND** — nghĩa là tất cả các trạng thái con phải thành công.  
- Với mỗi trạng thái con sinh ra, thuật toán gọi lại `OR-SEARCH` để kiểm tra xem có thể đạt được goal không.  
- Nếu bất kỳ trạng thái con nào thất bại → toàn bộ AND node đó thất bại.  
- Nếu tất cả đều thành công → kết hợp các kế hoạch con lại và trả về.  

**Điều Kiện Dừng:**  
- Nếu đạt được goal state → trả về kế hoạch rỗng `[]` (đã hoàn thành).  
- Nếu phát hiện vòng lặp (trạng thái đã xuất hiện trong đường đi hiện tại) → bỏ qua nhánh đó để tránh lặp vô tận.  

**Kết Thúc:**  
- Nếu có ít nhất một kế hoạch hợp lệ → in ra kế hoạch hoàn chỉnh.  
- Nếu không có kế hoạch nào dẫn đến goal → thông báo không tìm thấy lời giải.  

---

## VI. Nhóm Thuật Toán Tìm Kiếm Trong Môi Trường Không Quan Sát Được

### 1. Belief Search

![demo-belief](gif/belief.gif)

-- **Lý Thuyết**  
* **Khái Niệm:** tìm kiếm trong không gian niềm tin (belief states), mỗi belief là một tập các trạng thái vật lý có thể xảy ra.  
* **Cách Hoạt Động:**  
  - đại diện niềm tin hiện tại (set hoặc phân phối), mở rộng niềm tin theo các hành động và mẫu quan sát (update belief),  
  - tìm chuỗi hành động tối ưu trong không gian niềm tin thay vì không gian trạng thái vật lý.  
* **Ưu Điểm:**  
  - cho phép ra quyết định khi môi trường không quan sát hoàn toàn hoặc có sai số cảm biến.  
* **Nhược Điểm:**  
  - không gian belief thường rất lớn, tính toán nặng.  
* **Độ Phức Tạp:**  
  - thời gian: tăng theo lũy thừa của số trạng thái khả dĩ trong không gian belief  
  - trong đó kích thước không gian belief phụ thuộc số trạng thái vật lý `|S|` và chiều sâu kế hoạch `t`, thường dẫn đến `O(|S|^t)` trong trường xấu nhất.  

-- **Ứng Dụng Trong Game Đặt 8 Quân Xe - Hàm `belief_search()`:**

**Khởi Tạo Trạng Thái Niềm Tin Ban Đầu:**  
- Mỗi hàng đều có tất cả các cột khả thi `[0..n-1]`, chưa có ràng buộc nào được áp dụng.  

**Bắt Đầu Tìm Kiếm Đệ Quy:**  
- Tại mỗi hàng, thuật toán thử đặt quân vào từng cột khả thi trong danh sách của hàng đó.  
- Mỗi lần đặt quân, thuật toán cập nhật lại danh sách cột khả thi của các hàng phía dưới bằng cách loại bỏ cột vừa được chọn (vì đã bị chiếm).  
- Sau đó, đệ quy sang hàng kế tiếp với danh sách khả năng mới được cập nhật.  

**Khi Đạt Tới Hàng Cuối Cùng (`row = n`):**  
- Lưu lại lời giải hiện tại, được xem như một belief state hợp lệ.  

**Sau Khi Duyệt Hết:**  
- Thuật toán tổng hợp toàn bộ các belief states đã tìm được.  
- Chọn ra belief state tốt nhất (trong đoạn code là trạng thái có cột đầu tiên nhỏ nhất).  
