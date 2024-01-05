def customMatchEntity(match) -> dict:
    return {
        "_id": str(match["_id"]),
        "Tr1": int(match["Tr1"]),
        "Tr2": int(match["Tr2"]),
        "Tr1S1": int(match["Tr1S1"]),
        "Tr2S1": int(match["Tr2S1"]),
        "Tr1S2": int(match["Tr1S2"]),
        "Tr2S2": int(match["Tr2S2"]),
        "Tr1S3": int(match["Tr1S3"]),
        "Tr2S3": int(match["Tr2S3"]),
        "T1": match["T1"],
        "T2": match["T2"],
        "Finished": bool(match["Finished"]),
    }


def customMatchesEntity(matches) -> list[dict]:
    return [customMatchEntity(match) for match in matches]
