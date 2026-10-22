def parse_student(line):
    parts = line.strip().split(",")
    if len(parts) != 2:
        raise ValueError("字段数量不为 2")
    name, score_s = parts[0].strip(), parts[1].strip()
    if not name:
        raise ValueError("姓名为空")
    score = int(score_s) # 这里可能会报错，交给外面捕获
    if not (0 <= score <= 100):
        raise ValueError("成绩超出 0~100")
    return {"name": name, "score": score}