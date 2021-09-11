import gspread
def anna_taulukko(worker_tunnukset: str, taulukko: str) -> gspread.models.Spreadsheet:
    gc =gspread.service_account(filename=worker_tunnukset)
    sh = gc.open_by_key(taulukko)
    return sh

def lue(taulukko, lehti: str, solu: str) -> str:
    worksheet = taulukko.worksheet(lehti)
    return worksheet.acell(solu).value
    