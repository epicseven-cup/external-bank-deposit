%% Copyright (c) 2025-2025, Jacky <jackylin616@gmail.com>
%%
%% Permission to use, copy, modify, and/or distribute this software for any
%% purpose with or without fee is hereby granted, provided that the above
%% copyright notice and this permission notice appear in all copies.

-module(external_bank_deposit).

inets:start(),

get_current_score(Url) ->
	case httpc:request(get, {Url, []}, [], []) of
		{ok, {StatusLine, [HttpHeader], HttpBodyResult}} ->
	.
