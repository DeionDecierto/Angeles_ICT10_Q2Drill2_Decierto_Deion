from pyscript import document

grade_7 = {"Zild Benitez", "Badjao Castro"}
grade_8 = {"Nataliya Batumbakal", "Mark Santos Loriz Magante Herrington"}
grade_9 = {"Blaster Silonga", "Unique Salonga"}
grade_10 = {"John Doe", "Jason Duval"}
new_members = set()

def update_display():
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_members
    document.querySelector("#output").innerHTML = f"""
        <h3>All Club Members:</h3>
        <p>{', '.join(master_set)}</p>
        <p><strong>Total Members:</strong> {len(master_set)}</p>
    """

def add_member(event):
    first = document.querySelector("#first-name").value.strip()
    last = document.querySelector("#last-name").value.strip()
    entry = {f"{first} {last}".strip()} - {""}
    global new_members
    new_members |= entry
    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""
    update_display()

update_display()