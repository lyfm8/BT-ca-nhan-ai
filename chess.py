import tkinter as tk
from collections import deque
import random
import heapq
import math
from tkinter import ttk


root = tk.Tk()
root.title("Giao dien ban co")
root.configure(background='white')

root.minsize(1600,800)
root.update_idletasks()

window_width = root.winfo_width()
window_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

n = 8
k = n // 2
STEP_DELAY_DEFAULT = 500  # ms giữa mỗi hàng khi hiển thị

def create_widgets(parent, widget_type, **options):
    return widget_type(parent, **options)

def create_button(parent, color, text='', **options):
    return create_widgets(parent, tk.Button, bg=color, bd=0, width=4, height=1,
                          text=text, font=('Arial', 20, 'bold'), **options)

# --- goal state ---
goal_cols = [None] * n

def is_valid_goal_state():
    if None in goal_cols:
        return False
    if len(set(goal_cols)) != n:
        return False
    return True

def place_rook_goal_state(r, c, frame):
    global goal_cols
    if goal_cols[r] is not None:
        return
    if c in goal_cols:
        return
    goal_cols[r] = c
    # cập nhật lại hiển thị bàn cờ mục tiêu
    two_chessboard(root, frame, solution=goal_cols, put_rook=True, rook_goal_text=True)
    update_buttons_state()

def generate_random_goal():
    global goal_cols
    # sinh hoán vị 0..7
    goal_cols = random.sample(range(n), n)
    # vẽ lại bàn cờ mục tiêu
    two_chessboard(root, frame_rook_goal, solution=goal_cols,
                   put_rook=True, rook_goal_text=True)
    # enable các nút giải thuật
    update_buttons_state()




############# cost
def cost_function(solution):
    # nếu solution rỗng hoặc goal chưa đầy, tránh lỗi: ta trả cost lớn
    if not solution or None in goal_cols:
        return float('inf')
    total_cost = 0
    for r, col in enumerate(solution):
        total_cost += abs(goal_cols[r] - col)
    return total_cost

########## Algorithms (each returns final solution list) ##########

def bfs_rooks():
    log_message("=== Bắt đầu BFS ===")
    queue = deque([[]])
    step = 0

    while queue:
        state = queue.popleft()
        step += 1
        log_message(f"[Bước {step}] Mở rộng trạng thái: {state}")

        if len(state) == n:
            log_message(f"🎯 Tìm thấy nghiệm cuối cùng: {state}")
            return state

        cols = list(range(n))
        random.shuffle(cols)
        expanded = 0
        for col in cols:
            if col not in state:
                new_state = state + [col]
                queue.append(new_state)
                expanded += 1
                log_message(f" ➜ Thêm node con: {new_state}")

        if expanded == 0:
            log_message(" (Không có node con nào hợp lệ)")

    log_message("❌ BFS kết thúc: không tìm thấy nghiệm")
    return None


def dfs_rooks():
    log_message("=== Bắt đầu DFS ===")
    stack = deque([[]])
    step = 0

    while stack:
        state = stack.pop()
        step += 1
        log_message(f"[Bước {step}] Mở rộng trạng thái: {state}")

        if len(state) == n:
            log_message(f"🎯 Tìm thấy nghiệm cuối cùng: {state}")
            return state

        cols = list(range(n))
        random.shuffle(cols)
        expanded = 0
        for col in cols:
            if col not in state:
                new_state = state + [col]
                stack.append(new_state)
                expanded += 1
                log_message(f" ➜ Thêm node con: {new_state}")

        if expanded == 0:
            log_message(" (Không có node con nào hợp lệ)")

    log_message("❌ DFS kết thúc: không tìm thấy nghiệm")
    return None


def ucs_rooks():
    log_message("=== Bắt đầu UCS ===")
    pq = [(0, [])]
    step = 0

    while pq:
        cost, state = heapq.heappop(pq)
        step += 1
        log_message(f"[Bước {step}] Mở rộng trạng thái: {state} (cost = {cost})")

        if len(state) == n:
            log_message(f"🎯 Tìm thấy nghiệm cuối cùng: {state} (tổng cost = {cost})")
            return state

        expanded = 0
        for col in range(n):
            if col not in state:
                new_state = state + [col]
                new_cost = cost_function(new_state)
                heapq.heappush(pq, (new_cost, new_state))
                expanded += 1
                log_message(f" ➜ Thêm node con: {new_state} (cost = {new_cost})")

        if expanded == 0:
            log_message(" (Không có node con nào hợp lệ)")

    log_message("❌ UCS kết thúc: không tìm thấy nghiệm")
    return None

def dls_rooks(limit=8):
    def dls(state, depth):
        if len(state) == n:
            return state
        if depth == limit:
            return None
        for c in range(n):
            if c not in state:
                res = dls(state + [c], depth + 1)
                if res:
                    return res
        return None
    return dls([], 0)

def check_goal_state(state):
    # an toàn: nếu goal chưa đầy thì không match
    if None in goal_cols:
        return False
    if len(state) != len(goal_cols):
        return False
    for i in range(len(state)):
        if state[i] != goal_cols[i]:
            return False
    return True

def id_dfs_rooks(limit):
    stack = deque([[]])
    while stack:
        state = stack.pop()
        if len(state) == n:
            if check_goal_state(state):
                return state
            continue
        if len(state) < limit:
            for col in range(n):
                if col not in state:
                    stack.append(state + [col])
    return None

def id_rooks():
    for limit in range(1, n+1):
        res = id_dfs_rooks(limit)
        if res:
            return res
    return None

def greedy_search_rooks():
    cols = list(range(n))
    state = []
    for row in range(n):
        # chọn c sao cho cost(state + [c]) nhỏ nhất
        best_col = min(cols, key=lambda c: cost_function(state + [c]))
        state.append(best_col)
        cols.remove(best_col)
    return state

def a_star_search():
    pq = [(0, 0, [])]  # (f, g, state)
    seen = set()
    while pq:
        f, g, state = heapq.heappop(pq)
        tup = tuple(state)
        if tup in seen:
            continue
        seen.add(tup)
        if len(state) == n:
            return state
        for col in range(n):
            if col not in state:
                new_state = state + [col]
                new_g = g + 1
                new_h = cost_function(new_state)
                new_f = new_g + new_h
                heapq.heappush(pq, (new_f, new_g, new_state))
    return None

def get_neighbors(state):
    neighbors = []
    # khi state có ít phần tử, ta vẫn sinh neighbor bằng cách hoán đổi
    for i in range(len(state)):
        for j in range(i+1, len(state)):
            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)
    return neighbors

def hill_climbing():
    state = list(range(n))
    random.shuffle(state)
    cur_cost = cost_function(state)
    while True:
        neighbors = get_neighbors(state)
        if not neighbors:
            return state
        neighbors_cost = []
        for nb in neighbors:
            cost = cost_function(nb)
            neighbors_cost.append((cost, nb))
        best_cost, best_neighbor = min(neighbors_cost, key=lambda x: x[0])
        if best_cost < cur_cost:
            state, cur_cost = best_neighbor, best_cost
        else:
            return state

def beam_search(k):
    beam = [(0, [])]
    for row in range(n):
        candidates = []
        for cost, state in beam:
            for col in range(n):
                if col not in state:
                    new_state = state + [col]
                    new_h = cost_function(new_state)
                    candidates.append((new_h, new_state))
        if not candidates:
            break
        # lấy k nhỏ nhất (trả tuple (cost, state))
        beam = heapq.nsmallest(k, candidates, key=lambda x: x[0])
    # chọn best trong beam
    if beam:
        best_cost, best_state = min(beam, key=lambda x: x[0])
        return best_state
    return None

def heuristic_conflict(state):
    h=0
    for i in range(len(state)-1):
        for j in range (i+1, len(state)):
            if state[i] == state[j]:
                h+=1
    return h

def simulated_annealing(T, T_min, alpha):
    state = random.choices(range(8), k=8)
    while T > T_min:
        neighbors = state[:]
        random_pos = random.randrange(len(state))
        neighbors[random_pos] = random.randint(0, 7)

        delta = heuristic_conflict(neighbors) - heuristic_conflict(state)

        if delta <= 0:
            state = neighbors
        else:
            P = math.exp(-delta / T)
            if random.random() < P:
                state = neighbors

        if check_goal_state(state):
            return state
        T *= alpha  # làm nguội

    return None

def genetic_algorithm(population_size, max_generations):
    population = []
    for i in range(population_size):
        population.append(random.choices(range(8), k=8))

    for gen in range(max_generations):
        for individual in population:
            if heuristic_conflict(individual) == 0:
                return individual

        dad, mom = heapq.nsmallest(2, population, key=heuristic_conflict)

        child1 = dad[0:4] + mom[4:8]
        child2 = dad[4:8] + mom[0:4]

        child_best = min(child1, child2, key=heuristic_conflict)

        if random.random() < 0.1:
            pos = random.randrange(8)
            child_best[pos] = random.randint(0, 7)

        new_population = [child_best]
        while len(new_population) < population_size:
            list_p = random.choices(range(8), k=8)
            new_population.append(list_p)

        population = new_population


    best_state = min(population, key=heuristic_conflict)
    return best_state




def sensorless():
    belief_states = []

    def search(row, col_available, current_sol):
        if row == n:
            belief_states.append(current_sol.copy())
            return

        for col in col_available[row]:
            new_col_available = []
            for r in range(row + 1, n):
                allowed = [c for c in col_available[r] if c != col]
                new_col_available.append(allowed)
            search(row + 1, col_available[:row + 1] + new_col_available, current_sol + [col])

    # tất cả các cột khả thi ở mỗi hàng
    initial_col = [list(range(n)) for _ in range(n)]
    search(0, initial_col, [])
    # ví dụ chọn “best state” theo cột đầu tiên nhỏ nhất
    best_state = min(belief_states, key=lambda x: x[0])
    return best_state[0]



def is_goal(state):
    return len(state) == n

def is_cycle(state, path):
    return state in path

def actions(state):
    row = len(state)
    used_cols = set(state)
    moves = []
    for col in range(n):
        if col not in used_cols:
            moves.append(col)
    return moves

def results(state, action):
    new_state = state + [action]
    return [new_state]

def and_or_search():
    return or_search([], [])

def or_search(state, path):
    if is_goal(state):
        return []
    if is_cycle(state, path):
        return None
    for action in actions(state):
        plan = and_search(results(state, action), path + [state])
        if plan is not None:
            return [action] + plan
    return None

def and_search(states, path):
    plans = []
    for s in states:
        plan = or_search(s, path)
        if plan is None:
            return None  # nếu 1 nhánh fail → toàn bộ fail
        plans.extend(plan)
    return plans


def csp():
    solutions = []

    def forward_checking(row, current_sol, col_available):
        if row == n:
            solutions.append(current_sol.copy())
            return

        for col in col_available[row]:
            # tạo bản sao của col_available để forward checking
            new_col_available = []
            valid = True
            for r in range(row+1, n):
                allowed = [c for c in col_available[r] if c != col]
                if not allowed:
                    valid = False  # không còn giá trị khả thi
                    break
                new_col_available.append(allowed)

            if valid:
                forward_checking(row+1, current_sol + [col], col_available[:row+1] + new_col_available)

    # khởi tạo miền giá trị cho mỗi hàng
    initial_col = [list(range(n)) for _ in range(n)]
    forward_checking(0, [], initial_col)
    return solutions[0]

def ac3():
    domains = {r: set(range(n)) for r in range(n)}
    queue = [(xi, xj) for xi in range(n) for xj in range(n) if xi != xj]

    while queue:
        xi, xj = queue.pop(0)
        if revise(domains, xi, xj):
            log_message(f"Revise({xi},{xj}) -> {domains[xi]}")
            if not domains[xi]:
                log_message("Domain rỗng -> fail")
                return None
            for xk in range(n):
                if xk != xi and xk != xj:
                    queue.append((xk, xi))

    solution = []
    used = set()

    def backtrack(r):
        if r == n:
            return True
        log_message(f"==> Đang xét hàng {r}, domain = {domains[r]}")
        for c in domains[r]:
            if c not in used:
                log_message(f"Thử đặt xe tại ({r},{c})")
                solution.append(c)
                used.add(c)
                if backtrack(r+1):
                    return True
                log_message(f"Backtrack: bỏ ({r},{c})")
                solution.pop()
                used.remove(c)
        log_message(f"Không có lựa chọn hợp lệ cho hàng {r}, quay lui")
        return False

    if backtrack(0):
        log_message(f"Nghiệm cuối cùng: {solution}")
        return solution
    else:
        log_message("Không tìm được nghiệm hợp lệ sau AC-3")
        return None


def revise(domains, xi, xj):
    """Loại bỏ giá trị khỏi domain[xi] nếu không có giá trị nào ở xj khác nó"""
    removed = False
    to_remove = set()
    for a in domains[xi]:
        if not any(a != b for b in domains[xj]):
            to_remove.add(a)
    if to_remove:
        domains[xi] -= to_remove
        removed = True
    return removed




################ UI drawing ################

def reset_board(frame):
    """
    Xoá toàn bộ quân xe trên bàn cờ nhưng giữ nguyên ô cờ.
    """
    for widget in frame.winfo_children():
        # chỉ reset button (ô cờ), không xoá luôn
        if isinstance(widget, tk.Button):
            widget.config(text="")
        # xoá nhãn chi phí hoặc nhãn phụ
        elif isinstance(widget, tk.Label):
            widget.destroy()


def two_chessboard(parent, frame, solution=None,
                   put_rook_goal=False, put_rook=False,
                   show_cost=False, rook_goal_text=False,
                   step_by_step=False, delay=STEP_DELAY_DEFAULT):
    """
    - Nếu step_by_step=True và solution là full list: sẽ hiển thị kết quả từng hàng 1
      (chỉ dùng solution[:row] để vẽ).
    - Nếu step_by_step=False: vẽ bình thường (có thể vẽ partial solution).
    """

    def draw_board(current_solution):
        reset_board(frame)
        # vẽ n x n (dùng n global)
        for r in range(n):
            for c in range(n):
                color = 'white' if (r + c) % 2 == 0 else 'darkgoldenrod'
                text = ""
                # vẽ quân (chỉ khi hàng đã có kết quả)
                if put_rook and current_solution and r < len(current_solution):
                    val = current_solution[r]
                    if val is not None and val == c:
                        text = '\u2656'
                if rook_goal_text:
                    button = create_button(
                        frame, color, text=text,
                        command=lambda r=r, c=c: place_rook_goal_state(r, c, frame)
                    )
                else:
                    button = create_button(frame, color, text=text)
                button.grid(row=r, column=c)
        # cost (dùng current_solution nếu có)
        if show_cost and current_solution:
            cost = cost_function(current_solution)
            tk.Label(frame, text=f"Chi phí: {cost}",
                     font=('Arial', 14, 'bold'),
                     bg='gold').grid(row=n, column=0, columnspan=n, pady=5)
        if rook_goal_text:
            tk.Label(frame, text="Bàn cờ mục tiêu",
                     font=('Arial', 14, 'bold'),
                     bg='gold').grid(row=n+1, column=0, columnspan=n, pady=5)

    # nếu step_by_step True và solution là full list -> hiển thị từng hàng 1
    if step_by_step and solution and len(solution) == n:
        def step(row):
            # row là số hàng hiện đang hiển thị (1..n)
            if row > n:
                return
            draw_board(solution[:row])
            # tiếp tục sau delay
            frame.after(delay, lambda: step(row + 1))
        step(1)
    else:
        # vẽ bình thường (solution có thể partial)
        draw_board(solution)

################ GUI layout ################

frame_boards = tk.Frame(root, bg='white')
frame_boards.pack(padx=10, pady=20)

frame_rook = tk.Frame(frame_boards, bg='white', bd=2, relief="solid")
frame_rook.pack(side=tk.LEFT, padx=10, pady=5)
two_chessboard(root, frame_rook, put_rook=False, show_cost=True, solution=None)

frame_rook_goal = tk.Frame(frame_boards, bg='white', bd=2, relief="solid")
frame_rook_goal.pack(side=tk.LEFT, padx=20, pady=5)
two_chessboard(root, frame_rook_goal, solution=goal_cols, put_rook=True, rook_goal_text=True)

frame_button = tk.Frame(frame_boards, bg='white', bd=0)
frame_button.pack(side=tk.LEFT, padx=10, pady=5)

#log
frame_log = tk.Frame(root, bg='white')
frame_log.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

log_text = tk.Text(frame_log, wrap=tk.WORD, height=15, font=("Consolas", 11))
log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_log, command=log_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
log_text.config(yscrollcommand=scrollbar.set)

button_clear_log = tk.Button(
    frame_log,
    text="🧹 Clear Log",
    font=("Segoe UI", 11, "bold"),
    bg="lightcoral",
    fg="white",
    relief="raised",
    command=lambda: log_text.delete(1.0, tk.END)
)
button_clear_log.pack(side=tk.BOTTOM, anchor="e", padx=10, pady=5)

def log_message(msg):
    log_text.insert(tk.END, msg + "\n")
    log_text.see(tk.END)



# --- thay thế đoạn button_quanxe_xxx và update_buttons_state bằng code này ---

# hàm chạy theo tên thuật toán
def run_selected_algo(group, algo_name):
    algo_map = {
        # Uninformed
        "BFS": bfs_rooks,
        "DFS": dfs_rooks,
        "UCS": ucs_rooks,
        "DLS": lambda: dls_rooks(limit=n),
        "ID": id_rooks,

        # Informed
        "Greedy": greedy_search_rooks,
        "A*": a_star_search,

        # Local & Optimization
        "Hill-Climbing": hill_climbing,
        "Beam Search": lambda: beam_search(k),
        "Simulated Annealing": lambda: simulated_annealing(T=1000, T_min=1, alpha=0.99),
        "GA": lambda: genetic_algorithm(population_size=12, max_generations=1000),

        # CSP
        "csp": csp,
        "AC-3": ac3,

        # Planning
        "And-Or search": and_or_search,
        "Sensorless": sensorless,
    }

    if algo_name in algo_map:
        run_and_show(frame_rook, algo_map[algo_name])
    else:
        log_message(f"Thuật toán {algo_name} chưa được hỗ trợ.")


# frame chứa controls
frame_controls = tk.Frame(frame_boards, bg='white')
frame_controls.pack(side=tk.LEFT, padx=10, pady=5, fill="y")

# nút tạo bàn cờ mục tiêu ngẫu nhiên
button_random_goal = tk.Button(frame_controls, bg='lightyellow',
                               text='Tạo bàn cờ mục tiêu ngẫu nhiên',
                               font=("Segoe UI Symbol", 13, "bold"), width=30,
                               command=generate_random_goal)
button_random_goal.pack(pady=6)

# reset
button_reset_chessboard = tk.Button(frame_controls, bg='white', text='Reset chessboard',
                                    font=("Segoe UI Symbol", 13, "bold"), width=20,
                                    command=lambda: reset_board(frame_rook))
button_reset_chessboard.pack(pady=6)


# ===== các nhóm combobox =====

groups = {
    "Uninformed": ["BFS", "DFS", "UCS", "DLS", "ID"],
    "Informed": ["Greedy", "A*"],
    "Local & Optimization": ["Hill-Climbing", "Simulated Annealing", "Beam Search", "GA"],
    "CSP": ["csp", "AC-3"],
    "Planning": ["And-Or search", "Sensorless"]
}

def run_selected_algo(group, algo_name):
    algo_map = {
        # Uninformed
        "BFS": bfs_rooks,
        "DFS": dfs_rooks,
        "UCS": ucs_rooks,
        "DLS": lambda: dls_rooks(limit=n),
        "ID": id_rooks,

        # Informed
        "Greedy": greedy_search_rooks,
        "A*": a_star_search,

        # Local & Optimization
        "Hill-Climbing": hill_climbing,
        "Beam Search": lambda: beam_search(k),
        "Simulated Annealing": lambda: simulated_annealing(T=1000, T_min=1, alpha=0.99),
        "GA": lambda: genetic_algorithm(population_size=12, max_generations=1000),

        # CSP
        "csp": csp,
        "AC-3": ac3,

        # Planning
        "And-Or search": and_or_search,
        "Sensorless": sensorless,
    }

    if algo_name in algo_map:
        run_and_show(frame_rook, algo_map[algo_name])
    else:
        log_message(f"Thuật toán {algo_name} chưa hỗ trợ.")

combo_boxes = {}

for group_name, algos in groups.items():
    frame_group = ttk.LabelFrame(frame_controls, text=group_name)
    frame_group.pack(padx=5, pady=8, fill="x")

    cb = ttk.Combobox(frame_group, values=algos, state="readonly", font=("Segoe UI", 12))
    cb.current(0)
    cb.pack(side="left", padx=5, pady=5)
    combo_boxes[group_name] = cb

    btn_run = ttk.Button(frame_group, text="Run",
                         command=lambda g=group_name, cb=cb: run_selected_algo(g, cb.get()))
    btn_run.pack(side="left", padx=5)


def update_buttons_state():
    state = tk.NORMAL if is_valid_goal_state() else tk.DISABLED
    button_reset_chessboard.config(state=state)
    for cb in combo_boxes.values():
        cb.config(state="readonly" if state == tk.NORMAL else tk.DISABLED)






# helper to run algorithm, then show solution row-by-row
def run_and_show(frame, algo_fn, step_by_step=True, delay=STEP_DELAY_DEFAULT):
    # chạy thuật toán -> lấy solution (có thể lâu)
    solution = algo_fn()
    if solution is None:
        # hiển thị thông báo tạm thời
        reset_board(frame)
        tk.Label(frame, text="Không tìm được nghiệm", font=('Arial', 14, 'bold')).grid(row=n, column=0, columnspan= n, padx=10, pady=10)
        return
    # hiển thị theo từng hàng
    two_chessboard(root, frame, solution=solution, put_rook=True, show_cost=True,
                   step_by_step=step_by_step, delay=delay)



# disable algorithm buttons until goal completed
update_buttons_state()

root.mainloop()
