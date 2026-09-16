# Gera kb/VERIFICACAO_VISUAL.md com o que foi visto, como foi conferido e o que ficou de fora.
import json, os, glob, re
K=os.path.expanduser("~/Downloads/apple-design-kb")
rep=json.load(open(f"{K}/kb/visual_logs/verificacao_codigos.json")); per=rep["per_video"]
man={v["id"]:v for v in json.load(open(f"{K}/raw/video_manifest.json"))}
vid=[k for k in per if not k.startswith("hig-")]; hig=[k for k in per if k.startswith("hig-")]
comp=lambda ks: [k for k in ks if per[k]["verified"]==per[k]["sheets"]]
semmidia=[v for v in man if not (man[v].get("sd") or man[v].get("m3u8"))]
sint_v=len(glob.glob(f"{K}/kb/visual_sintese_videos/*.md")); sint_h=len(glob.glob(f"{K}/kb/visual_sintese_hig/*.md"))
div=0
for f in glob.glob(f"{K}/kb/visual_sintese_hig/*.md")+glob.glob(f"{K}/kb/visual_sintese_videos/*.md"):
    if re.search(r"^Divergências",open(f).read(),flags=re.M): div+=1
L=[]
L.append("# Verificação da camada visual\n")
L.append("Como funciona a prova: cada folha de quadros e cada folha de ilustrações recebeu, na própria imagem, um código de cinco caracteres derivado de uma chave secreta guardada fora da base. O código só pode ser obtido olhando a imagem. O agente que viu a folha anotou o código, e a conferência recalcula o código esperado e compara.\n")
L.append("## Números\n")
L.append("| Item | Valor |\n|---|---|")
L.append(f"| Vídeos com arquivo no site | {len(man)-len(semmidia)} |")
L.append(f"| Vídeos processados em folhas | {len(vid)} |")
L.append(f"| Folhas de quadros | {sum(per[k]['sheets'] for k in vid)} |")
L.append(f"| Folhas conferidas | {sum(per[k]['verified'] for k in vid)} |")
L.append(f"| Vídeos assistidos por inteiro | {len(comp(vid))} |")
L.append(f"| Unidades do HIG (páginas de ilustração e vídeos de demonstração) | {len(hig)} |")
L.append(f"| Folhas do HIG conferidas | {sum(per[k]['verified'] for k in hig)} de {sum(per[k]['sheets'] for k in hig)} |")
L.append(f"| Códigos que não bateram | {rep['codes_wrong']} |")
L.append(f"| Sínteses visuais escritas | {sint_v} de vídeo e {sint_h} do HIG |")
L.append(f"| Sínteses com divergência registrada entre imagem e descrição oficial | {div} |")
L.append(f"| Vídeos sem arquivo no site, não assistidos | {len(semmidia)} |\n")
inc=[k for k in vid if per[k]["verified"]!=per[k]["sheets"]]
L.append("## O que ficou incompleto\n")
L.append("Nenhum vídeo processado ficou com folha sem conferir." if not inc else "\n".join(f"- {k}: {per[k]['verified']} de {per[k]['sheets']} folhas" for k in inc))
L.append("\n## Vídeos sem arquivo no site\n")
L.append("Estes não têm vídeo nem transcrição na origem, então não foram assistidos nem receberam cartão:\n")
L.append("\n".join(f"- {v}" for v in sorted(semmidia)))
L.append("\n## Limites do método\n")
L.append("1. As folhas trazem um quadro por mudança de cena e pelo menos um a cada 12 segundos, não todos os quadros do vídeo. Movimento contínuo aparece como diferença entre quadros parados.")
L.append("2. Efeitos rápidos podem não aparecer entre dois quadros. Quando isso ocorreu, está registrado na nota da folha.")
L.append("3. As ilustrações do HIG foram vistas na versão clara; a versão escura entrou nas páginas de cor, modo escuro, materiais e ícones.")
L.append("4. Miniaturas e ícones que a página só usa como link para outras páginas ficaram de fora.")
open(f"{K}/kb/VERIFICACAO_VISUAL.md","w").write("\n".join(L)+"\n")
print("relatório escrito com", len(comp(vid)), "vídeos completos e", rep["codes_wrong"], "códigos errados")
