import time


def format_date() -> None:
    current_time = time.time()

    int_part = int(current_time)
    dec_part = current_time - int_part

    int_part_formated = format(int_part, ',')
    dec_part_formated = f"{dec_part:.4f}"[2:]

    seconds_formated = f"{int_part_formated}.{dec_part_formated}"
    scientific_notation = f"{current_time:.2e}"
    human_readable = time.strftime("%b %d %Y", time.localtime(current_time))

    print(f"Seconds since January 1, 1970: {seconds_formated} or \
        {scientific_notation} in scientific notation")
    print(f"{human_readable}")


if __name__ == "__main__":
    format_date()
