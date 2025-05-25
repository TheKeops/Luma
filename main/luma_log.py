import datetime

def save_log(title=None, content=None, type=None):

    if type.strip().upper() == "LOG":
        with open("main/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA INFO [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")

    elif type.strip().upper() == "WARNING":
        with open("main/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA WARNING [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")

    elif type.strip().upper() == "ERROR":
        with open("main/log/log.log", "a", encoding="utf-8") as f:
            f.writelines(f"- LUMA ERROR [{datetime.datetime.now().strftime('%H:%M:%S')}] : TITLE : {title} - COMMENT : {content}\n")
