--zzrlc = Zam Zam Repo Lua Client
--
--
--
--
--
--------------------------------- 


local version = 0.1 
local tArgs = {...}
local url = 'http://127.0.0.1:7000/raw/'
local headers = {
	['username'] = 'admin',
	['pasword'] = 'admin@14'
}
if tArgs[1] == 'get' then 
	data = http.get(url..tArgs[2])
	
end 
