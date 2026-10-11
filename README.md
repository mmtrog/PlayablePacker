# Playable Packer

Turns one Luna (Unity Playworks) playable export into a build for each ad network: AppLovin, Unity Ads, ironSource, generic MRAID, Meta (Facebook), Google Ads, Mintegral, Liftoff (Vungle) and TikTok.

For each network it:
- injects a bridge script that routes the CTA (`mraid.open`, `FbPlayableAd.onCTAClick`, `ExitApi.exit`, `window.install`, `playableSDK.openAppStore`, store links opened with `window.open`) and the game-end hook `window.__playableGameEnd()` to that network's API;
- adds the tags the network needs (`mraid.js`, Google's ExitApi script and `ad.orientation`, TikTok's `config.json`) and drops other networks' script tags;
- packs it as the `.html` or `.zip` the network takes, shows the size against its cap and lists outside requests;
- tests the CTA in a sandboxed frame with the network's API stubbed.

Everything runs in the browser: files are never uploaded. Still check each file in the network's own preview or validator before a campaign.

## Use
1. Open the GitHub Pages site (or `docs/index.html` locally).
2. Drop a Luna MRAID / AppLovin export (`.html` or `.zip`) and fill in the store links.
3. Pick the networks and click **Download selected**. You get one `.zip` with a folder per network, each holding the file to upload there:

```
<name>-networks.zip
├── AppLovin/<name>-applovin.html
├── UnityAds/<name>-unity.html
├── ironSource/<name>-ironsource.html
├── MRAID/<name>-mraid.html
├── Meta/<name>-facebook.html
├── GoogleAds/<name>-google.zip      (index.html)
├── Mintegral/<name>-mintegral.zip   (index.html)
├── Liftoff/<name>-vungle.zip        (index.html)
└── TikTok/<name>-tiktok.zip         (index.html + config.json)
```

For Mintegral `gameEnd()` and Liftoff `complete`, the game must call `window.__playableGameEnd()` when it ends.

## Files
- `playable-packer.html`: the tool (source). Written without doctype/charset/viewport so it can also be published as a claude.ai artifact.
- `docs/index.html`: the standalone page served by GitHub Pages, generated from the source.
- `make-standalone.py`: regenerates `docs/index.html`. Run after every edit:

```
python3 make-standalone.py
```

For each release, add an entry at the top of the **Changelog** list in `playable-packer.html` (`<li class="rel" data-version="vX.Y">`). The version shown in the page header comes from the newest entry.

## Host on GitHub Pages
Settings → Pages → Build and deployment: **Deploy from a branch**, branch `main`, folder `/docs`. The site is served at `https://<user>.github.io/<repo>/`.
