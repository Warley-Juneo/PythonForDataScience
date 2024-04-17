def ft_tqdm(lst: range) -> None:
    total = len(lst)

    for i, item in enumerate(lst, 1):
        progress = int((i/total) * 100)
        print(f'\r{progress}%|{"█" * progress}{" " * (100 - progress)}|{i}/\
            {total}', end='')
        yield item
