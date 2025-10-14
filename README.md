* CÁC THUẬT TOÁN TÌM KIẾM TRONG AI


I. Nhóm thuật toán tìm kiếm không có thông tin

1. Breadth-First Search (BFS)
![demo-bfs](gif/bfs.gif)

* Khái niệm: tìm kiếm theo chiều rộng, duyệt từng mức của cây trạng thái từ gốc ra ngoài.  
* Cách hoạt động:
  - bắt đầu từ nút gốc, dùng hàng đợi để lưu các nút chờ mở rộng,
  - lần lượt mở rộng tất cả nút ở độ sâu 0, rồi 1, rồi 2,... cho đến khi tìm được đích.  
* Ưu điểm:
  - tìm được lời giải ngắn nhất nếu chi phí các bước đi bằng nhau,
  - đơn giản, trực quan.  
* Nhược điểm:
  - tốn nhiều bộ nhớ khi không gian trạng thái lớn.  
* Độ phức tạp:
  - thời gian: O(b^d)
  - bộ nhớ: O(b^d)
  - trong đó b là hệ số phân nhánh (branching factor), d là độ sâu của lời giải.

2. Depth-First Search (DFS)
![demo-dfs](gif/dfs.gif)

* Khái niệm: tìm kiếm theo chiều sâu, đi sâu vào một nhánh cho đến khi gặp đích hoặc bế tắc.  
* Cách hoạt động:
  - dùng ngăn xếp (hoặc đệ quy) để theo dõi đường đi hiện tại,
  - mở rộng nút con đầu tiên liên tiếp; khi không thể mở rộng, quay lui (backtrack) lên nút cha.  
* Ưu điểm:
  - tốn ít bộ nhớ hơn BFS,
  - có thể tìm lời giải nhanh khi nó nằm sâu nhưng ở nhánh đầu.  
* Nhược điểm:
  - không đảm bảo tìm lời giải tối ưu,
  - có thể rơi vào vòng lặp nếu không kiểm soát.  
* Độ phức tạp:
  - thời gian: O(b^m)
  - bộ nhớ: O(b * m)
  - trong đó b là hệ số phân nhánh, m là độ sâu tối đa của cây.

3. Uniform Cost Search (UCS)
![demo-ucs](gif/ucs.gif)

* Khái niệm: tìm kiếm theo chi phí, luôn mở rộng nút có chi phí đường đi g(n) nhỏ nhất trước.  
* Cách hoạt động:
  - dùng hàng đợi ưu tiên (priority queue) sắp theo g(n),
  - khi pop một nút đích từ hàng đợi, đảm bảo đó là đường đi chi phí nhỏ nhất.  
* Ưu điểm:
  - luôn tìm được nghiệm tối ưu nếu chi phí các bước là không âm.  
* Nhược điểm:
  - có thể tốn thời gian/bộ nhớ lớn nếu không có heuristic.  
* Độ phức tạp:
  - thời gian: O(b^(1 + ⌊C*/ε⌋))
  - bộ nhớ: O(b^(1 + ⌊C*/ε⌋))
  - trong đó b là hệ số phân nhánh, C* là chi phí của lời giải tối ưu, ε là kích thước bước chi phí nhỏ nhất (minimum step cost).

4. Depth-Limited Search (DLS)
![demo-dls](gif/dls.gif)

* Khái niệm: phiên bản của DFS với giới hạn độ sâu tối đa L.  
* Cách hoạt động:
  - thực hiện DFS nhưng không mở rộng các nút có độ sâu vượt quá L,
  - nếu đến độ sâu L mà chưa tìm thấy đích thì trả về failure (hoặc cut-off).  
* Ưu điểm:
  - tránh vòng lặp vô hạn khi không có kiểm tra visited, kiểm soát bộ nhớ.  
* Nhược điểm:
  - có thể bỏ sót lời giải nếu nằm sâu hơn L.  
* Độ phức tạp:
  - thời gian: O(b^L)
  - bộ nhớ: O(b * L)
  - trong đó b là hệ số phân nhánh, L là độ sâu giới hạn.

5. Iterative Deepening (ID)
![demo-id](gif/id.gif)

* Khái niệm: kết hợp ưu điểm của BFS (tối ưu theo bước) và DFS (bộ nhớ thấp) bằng cách lặp DLS với L tăng dần từ 0 tới d.  
* Cách hoạt động:
  - thực hiện DLS với L = 0, rồi L = 1, rồi L = 2,... cho đến khi tìm thấy lời giải,
  - mỗi lần lặp giống một DFS nhưng giới hạn sâu khác nhau.  
* Ưu điểm:
  - tìm được lời giải tối ưu như BFS nhưng chỉ dùng bộ nhớ như DFS.  
* Nhược điểm:
  - lặp lại nhiều lần các node ở các mức nông (tốn CPU).  
* Độ phức tạp:
  - thời gian: O(b^d)
  - bộ nhớ: O(b * d)
  - trong đó b là hệ số phân nhánh, d là độ sâu của lời giải.

II. Nhóm thuật toán tìm kiếm có thông tin

1. Greedy Best-First Search
![demo-greedy](gif/greedy.gif)

* Khái niệm: chọn mở rộng nút có heuristic h(n) nhỏ nhất — tức là nút "có vẻ" gần đích nhất.  
* Cách hoạt động:
  - dùng hàng đợi ưu tiên sắp theo h(n),
  - luôn mở rộng nút có h(n) thấp nhất, không xét g(n) (chi phí đã đi).  
* Ưu điểm:
  - nhanh trong nhiều trường hợp vì tập trung theo heuristic.  
* Nhược điểm:
  - không đảm bảo nghiệm tối ưu, dễ rơi vào bẫy heuristic (local optimum).  
* Độ phức tạp:
  - thời gian: O(b^d) (trường hợp xấu)
  - bộ nhớ: O(b^d)
  - trong đó b là hệ số phân nhánh, d là độ sâu của lời giải; hiệu năng thực tế phụ thuộc mạnh vào chất lượng hàm heuristic h(n).

2. A* Search
![demo-a_star](gif/a_star.gif)

* Khái niệm: kết hợp giữa chi phí thực tế g(n) và heuristic h(n) bằng f(n) = g(n) + h(n) để chọn nút mở rộng.  
* Cách hoạt động:
  - dùng hàng đợi ưu tiên sắp theo f(n),
  - mở rộng nút có f(n) nhỏ nhất; với heuristic *admissible* (không đánh giá quá thấp) thì A* tìm lời giải tối ưu.  
* Ưu điểm:
  - đầy đủ và tối ưu nếu h(n) là admissible; nếu h(n) còn *consistent* thì quá trình cập nhật đơn giản hơn.  
* Nhược điểm:
  - tốn bộ nhớ vì phải lưu open/closed lists; có thể nổ bộ nhớ trên không gian lớn.  
* Độ phức tạp:
  - thời gian: O(b^d) (trường hợp xấu; thực tế phụ thuộc chất lượng h)
  - bộ nhớ: O(b^d)
  - trong đó b là hệ số phân nhánh, d là độ sâu lời giải; hiệu năng cải thiện khi h càng gần giá trị thực của chi phí còn lại.

III. Nhóm thuật toán tìm kiếm cục bộ

1. Hill Climbing
![demo-hc](gif/hc.gif)

* Khái niệm: bắt đầu từ một trạng thái ban đầu, lặp tìm trạng thái lân cận tốt hơn theo hàm mục tiêu.  
* Cách hoạt động:
  - từ trạng thái hiện tại, sinh tất cả (hoặc một số) trạng thái lân cận,
  - chọn trạng thái có giá trị tốt nhất; nếu không có trạng thái tốt hơn thì dừng (có thể local optimum).  
* Ưu điểm:
  - đơn giản, nhanh cho các bài toán có không gian lớn nhưng cục bộ mượt.  
* Nhược điểm:
  - dễ kẹt ở cực trị địa phương, plateaus, hoặc rời local optimum.  
* Độ phức tạp:
  - thời gian: O(i * b)
  - bộ nhớ: O(n)
  - trong đó i là số vòng lặp (iterations), b là số lân cận mỗi bước, n là kích thước lưu trạng thái (hoặc kích thước input).

2. Simulated Annealing
![demo-sa](gif/sa.gif)

* Khái niệm: mở rộng hill climbing bằng cách cho phép chấp nhận các bước xấu với xác suất giảm dần (theo "nhiệt độ") để thoát local optimum.  
* Cách hoạt động:
  - tại mỗi bước, chọn ngẫu nhiên một trạng thái lân cận,
  - nếu tốt hơn thì chấp nhận; nếu xấu hơn thì chấp nhận với xác suất e^{-Δ/T}, giảm dần T theo lịch (schedule).  
* Ưu điểm:
  - có thể thoát local optimum và tìm gần tới global optimum nếu lịch giảm nhiệt hợp lý.  
* Nhược điểm:
  - cần tinh chỉnh lịch nhiệt độ và số bước; chậm nếu muốn đảm bảo chất lượng tốt.  
* Độ phức tạp:
  - thời gian: O(i * b)
  - bộ nhớ: O(n)
  - trong đó i là số vòng lặp, b là số lân cận, n là kích thước trạng thái.

3. Beam Search
![demo-beam](gif/beam.gif)

* Khái niệm: giữ lại tối đa k trạng thái tốt nhất (beam width) ở mỗi bước, thay vì giữ toàn bộ frontier.  
* Cách hoạt động:
  - từ k trạng thái hiện tại, sinh tất cả con của chúng,
  - chọn k trạng thái tốt nhất trong số đó làm trạng thái cho bước tiếp theo.  
* Ưu điểm:
  - tiết kiệm bộ nhớ hơn tìm kiếm toàn diện; nhanh hơn khi k nhỏ.  
* Nhược điểm:
  - không đảm bảo tìm lời giải tối ưu; nếu k quá nhỏ dễ mất nghiệm tốt.  
* Độ phức tạp:
  - thời gian: O(k * b * d)
  - bộ nhớ: O(k * d)
  - trong đó k là beam width, b là hệ số phân nhánh, d là độ sâu (số bước cần tìm).

4. Genetic Algorithm
![demo-ga](gif/ga.gif)

* Khái niệm: thuật toán tiến hóa dùng quần thể các cá thể, áp dụng chọn lọc, lai ghép, và đột biến để tiến đến nghiệm tốt.  
* Cách hoạt động:
  - khởi tạo quần thể kích thước P,
  - lặp: đánh giá fitness, chọn cá thể, lai ghép để tạo thế hệ mới, áp dụng đột biến, lặp G thế hệ.  
* Ưu điểm:
  - mạnh với không gian tìm kiếm lớn và đa cực trị, dễ song song hóa.  
* Nhược điểm:
  - nhiều siêu tham số cần tinh chỉnh; không đảm bảo tối ưu toàn cục.  
* Độ phức tạp:
  - thời gian: O(P * G * L)
  - bộ nhớ: O(P * L)
  - trong đó P là kích thước quần thể (population), G là số thế hệ (generations), L là chi phí đánh giá một cá thể (length / evaluation cost).

IV. Nhóm thuật toán tìm kiếm theo ràng buộc

1. Backtracking + Forward Checking
![demo-bfc](gif/bfc.gif)

* Khái niệm: thử gán giá trị cho biến theo thứ tự, quay lui khi mâu thuẫn, và dùng forward checking để loại bỏ giá trị không khả thi cho các biến còn lại.  
* Cách hoạt động:
  - chọn biến chưa gán, thử từng giá trị hợp lệ, cập nhật miền (domain) các biến chưa gán bằng forward checking,
  - nếu một biến có miền rỗng thì quay lui; tiếp tục đến khi gán đủ.  
* Ưu điểm:
  - giảm đáng kể không gian tìm kiếm so với brute force.  
* Nhược điểm:
  - vẫn có thể tốn thời gian nếu ràng buộc yếu hoặc thứ tự biến xấu.  
* Độ phức tạp:
  - thời gian: O(d^n) trong trường xấu nhất
  - trong đó n là số biến, d là kích thước miền giá trị trung bình.

2. AC-3 (Arc Consistency 3)
![demo-ac3](gif/ac3.gif)

* Khái niệm: thuật toán đạt tính khớp cung (arc consistency) cho các ràng buộc nhị phân, loại bỏ giá trị không còn khả thi.  
* Cách hoạt động:
  - đưa tất cả cung (Xi, Xj) vào hàng đợi,
  - lặp: lấy một cung, cô lập các giá trị không có đối ứng hợp lệ và cập nhật miền; nếu thay đổi thì thêm các cung liên quan vào hàng đợi.  
* Ưu điểm:
  - tiền xử lý tốt giúp backtracking hiệu quả hơn; giảm miền giá trị sớm.  
* Độ phức tạp:
  - thời gian: O(e * d^3)
  - trong đó e là số ràng buộc (số cung), d là kích thước miền giá trị lớn nhất.

V. Nhóm thuật toán tìm kiếm phân rã

1. And-Or Search
![demo-ao](gif/ao.gif)

* Khái niệm: mô hình cây gồm nút OR (chọn một hành động) và nút AND (phải giải quyết toàn bộ các nhánh con), phù hợp cho lập kế hoạch phân rã hoặc bài toán có cấu trúc con.  
* Cách hoạt động:
  - mở rộng theo kiểu and/or: với nút OR thử từng hành động (một trong các lựa chọn), với nút AND phải kết hợp nghiệm từ tất cả nhánh con,
  - dùng đệ quy và memoization để tránh lặp lại.  
* Độ phức tạp:
  - thời gian: thường là số mũ theo kích thước phân rã (exponential)
  - trong đó độ phức tạp phụ thuộc vào số lượng nhánh tại nút OR/AND và độ sâu phân rã.

VI. Nhóm thuật toán tìm kiếm trong môi trường không quan sát được

1. Belief Search
![demo-belief](gif/belief.gif)

* Khái niệm: tìm kiếm trong không gian niềm tin (belief states), mỗi belief là một tập các trạng thái vật lý có thể xảy ra.  
* Cách hoạt động:
  - đại diện niềm tin hiện tại (set hoặc phân phối), mở rộng niềm tin theo các hành động và mẫu quan sát (update belief),
  - tìm chuỗi hành động tối ưu trong không gian niềm tin thay vì không gian trạng thái vật lý.  
* Ưu điểm:
  - cho phép ra quyết định khi môi trường không quan sát hoàn toàn hoặc có sai số cảm biến.  
* Nhược điểm:
  - không gian belief thường rất lớn, tính toán nặng.  
* Độ phức tạp:
  - thời gian: tăng theo lũy thừa của số trạng thái khả dĩ trong không gian belief
  - trong đó kích thước không gian belief phụ thuộc số trạng thái vật lý |S| và chiều sâu kế hoạch t, thường dẫn đến O(|S|^t) trong trường xấu.

    