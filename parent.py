import os, subprocess, time, signal

try:
    # 创建子进程运行child.py
    # ps = subprocess.Popen(["python", "child.py"])
    # ps = subprocess.Popen(["ls", "-l"])
    for i in range(1,5):
        print("parent process start, PID: ", os.getpid())
        ps = subprocess.Popen(["python", "child.py"])
        time.sleep(1)

    # 使用SIGKILL信号终止子进程
    os.kill(ps.pid, signal.SIGKILL)

    # 等待子进程完全终止
    ps.wait()

    # 检查子进程是否已终止
    if ps.poll() is not None:
        print(f"子进程已终止，退出码: {ps.returncode}")
    else:
        print("子进程未能终止")
except Exception as e:
    print(f"发生异常: {e}")
finally:
    print("parent process end")
