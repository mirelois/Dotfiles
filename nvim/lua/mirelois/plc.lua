local open = io.open

local function read_file(path)
    local file = open(path, "rb") -- r read mode and b binary mode
    if not file then return "" end
    local content = file:read "*a" -- *a or *all reads the whole file
    file:close()
    return content:sub(1, -7)
end

vim.keymap.set("n", "<leader>ry", [[:TermExec cmd="python3 yacc.py <input >test1.vm" open=0<CR>]])
vim.keymap.set("n", "<leader>rv", [[:TermExec cmd="vms -g ]] .. read_file("./input") .. [[vm" open=0]])
vim.keymap.set("n", "<leader>ra",
    [[:TermExec cmd="python3 yacc.py <input >test1.vm && vms -g ]] .. read_file("./input") .. [[vm" open=0<CR>]])
vim.keymap.set("n", "<leader>?", "i¿")


