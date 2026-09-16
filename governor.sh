#!/bin/zsh
# Mantém o pipeline de vídeo e todos os filhos em prioridade de segundo plano (nice 20 + QoS background) até ele terminar.
desc() { local p=$1; echo $p; for c in $(pgrep -P $p); do desc $c; done; }
typeset -A seen
while root=$(pgrep -f "media_pipeline.py" | head -1) && [ -n "$root" ]; do
  for p in $(desc $root); do
    if [ -z "${seen[$p]}" ]; then renice -n 20 -p $p >/dev/null 2>&1; taskpolicy -b -p $p 2>/dev/null; seen[$p]=1; fi
  done
  sleep 5
done
echo "pipeline terminou, governador saiu"
