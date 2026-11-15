# Muse install

Copy this folder's `SKILL.md` and `skill.yaml`, plus the repo's `skills/`
tree, into one folder:

```bash
mkdir -p ~/workspace/custom-skills/sparkedin
cp muse-install/SKILL.md muse-install/skill.yaml ~/workspace/custom-skills/sparkedin/
cp -r skills ~/workspace/custom-skills/sparkedin/
```

The router `SKILL.md` reads the sub-skills from `skills/sp-*/SKILL.md`
relative to its own folder. The profile directory on Muse is
`~/workspace/linkedin/`.
