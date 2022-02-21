// CrossBerry - JAVASCRIPT

window.addEventListener('contextmenu', (event) => {
	event.preventDefault();
});

function site_get(item) {
	return localStorage.getItem(`crossberry-site-data-${item}`);
}

function discord_get(item) {
	return localStorage.getItem(`crossberry-user-data-${item}`);
}

function welcome() {
	if (discord_get("id") == "" || discord_get("id") == null) {
		localStorage.clear();
		location.replace('login-failure');
		return
	}
	
	avatar = document.getElementById("welcome-user-avatar");
	username = document.getElementById("welcome-user-name");

	username.innerHTML = discord_get("username");
	avatar.src = `https://cdn.discordapp.com/avatars/${discord_get("id")}/${discord_get("avatar")}.png`;
	// avatar.style.background = `${discord_get("banner_color")}bb`;
}

function logout() {
	localStorage.clear();
	document.body.innerHTML = `
		<div class="center-box">
			<i class="fa-solid fa-circle-notch fa-spin" id="login-spin"></i>
		</div>

		<div class="bg"></div>
	`;
	tick = 0;
	seconds = 3;
	if (site_get("qload") == "on") {
		seconds = -1;
	}
	ticker = window.setInterval(() => {
		if (tick > seconds) {
			window.clearInterval(ticker);
			location.replace("logout");
		}
		tick += 1;
	}, 1000);
}

function home() {
	user_options = document.getElementById('user-options');

	if (!(discord_get("id") == "" || discord_get("id") == null)) {
		user_options.innerHTML = `
			<button>
				Know More! <i class="fa-solid fa-graduation-cap"></i>
			</button>
			<button onclick="redirect('profile');">
				Account <i class="fa-solid fa-user"></i>
			</button>
			<button onclick="redirect('my-servers');">
				My Servers <i class="fa-solid fa-robot"></i>
			</button>
		`;
	}
}

function add_bot_redirect(permission_type) {
	client_id = "894131041390977074";
	permissions = 0;
	scope = "bot";
	
	permissions_selection = document.getElementById("permissions-selections");

	if (permission_type == "safe") {
		permissions = 0;
		permissions_selection.innerHTML = ``;
	} else if (permission_type == "default") {
		permissions = {{default_bot_permissions}};
		permissions_selection.innerHTML = ``;
	} else if (permission_type == "admin") {
		permissions = 8;
		permissions_selection.innerHTML = ``;
	} else if (permission_type == "custom-select") {
		permissions_selection.innerHTML = `
			<input type="checkbox"> Manage Messages<br>
			<input type="checkbox"> Connect Voice Channels<br>
			<button onclick="add_bot_redirect('custom');">
				Add Bot <i class="fa-solid fa-plus"></i>
			</button>
		`;
	} else if (permission_type == "custom") {
		permissions = {{default_bot_permissions}};
	}

	invite_url = `https://discord.com/api/oauth2/authorize?client_id=${client_id}&permissions=${permissions}&scope=${scope}`;
	
	if (permission_type !== "custom-select") {
		document.body.innerHTML = `
			<div class="center-box">
				<i class="fa-solid fa-circle-notch fa-spin" id="login-spin"></i>
			</div>

			<div class="bg"></div>
		`;

		tick = 0;
		seconds = 3;
		if (site_get("qload") == "on") {
			seconds = -1;
		}
		ticker = window.setInterval(() => {
			if (tick > seconds) {
				window.clearInterval(ticker);
				location.replace(invite_url);
			}
			tick += 1;
		}, 1000);
	}
}

function redirect_home() {
	document.body.innerHTML = `
		<div class="center-box">
			<i class="fa-solid fa-circle-notch fa-spin" id="login-spin"></i>
		</div>

		<div class="bg"></div>
	`;

	tick = 0;
	seconds = 2;
	if (site_get("qload") == "on") {
		seconds = -1;
	}
	ticker = window.setInterval(() => {
		if (tick > seconds) {
			window.clearInterval(ticker);
			location.href = '/';
		}
		tick += 1;
	}, 100);
}

function redirect(page) {
	document.body.innerHTML = `
		<div class="center-box">
			<i class="fa-solid fa-circle-notch fa-spin" id="login-spin"></i>
		</div>

		<div class="bg"></div>
	`;

	tick = 0;
	seconds = 3;
	if (site_get("qload") == "on") {
		seconds = -1;
	}
	ticker = window.setInterval(() => {
		if (tick > seconds) {
			window.clearInterval(ticker);
			location.href = page;
		}
		tick += 1;
	}, 100);
}

