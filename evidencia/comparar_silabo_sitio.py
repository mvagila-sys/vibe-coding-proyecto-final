import re,sys,json,unicodedata
js=open(sys.argv[1],encoding='utf-8').read()
U=re.search(r'var U = (\[.*?\]);\n',js,re.S).group(1)
U=json.loads(re.sub(r'([{,]\s*)(id|t|c):',r'\1"\2":',U))
MP=json.loads(re.search(r'var MP = (\[.*?\]);',js).group(1))
EV=json.loads(re.search(r'var EV = (\[.*?\]);',js).group(1))
# Transcrito del PDF «Sílabo — Competencias Humanas para el Futuro», pp. 2-4
S=[["La misión y el propósito como horizonte","Fundamentos del modelo educativo","La antropología y el humanismo integral","De la antropología a la estrategia","El rol del docente en este horizonte","Indicadores de la formación integral","Invitación a la reflexión"],
["Competencias humanas y modelo educativo","Habilidades blandas y competencias genéricas de la UTPL","La DPI y su relación con marcos internacionales (UNESCO, Foro Económico Mundial, OCDE, Tuning)","Resultados de aprendizaje de la asignatura","El proyecto de desarrollo personal","La relación entre modelo educativo y asignatura","Invitación a la reflexión"],
["El marco de competencias UTPL","La taxonomía UTPL como progresión del aprendizaje","Las rúbricas institucionales","Metodologías activas y evidencias de aprendizaje","Estrategias y actividades para integrar competencias genéricas en el aula","Camino hacia el microproyecto docente integrador"],
["Objetivo de la unidad","El microproyecto docente integrador","La importancia de la transversalidad","Actividad calificada de la unidad","Criterios de evaluación del microproyecto","Invitación final a la reflexión"]]
SMP=["Contexto de la asignatura y su aporte a los perfiles profesional y de egreso.","Resultado de aprendizaje seleccionado del plan docente.","Competencia genérica elegida.","Actividad integradora (componente específico y genérico).","Metodología activa aplicada y su justificación.","Evidencias esperadas del estudiante.","Rúbrica o instrumento de evaluación y forma de retroalimentación."]
SEV={"taller":20,"micro":40,"examen":20,"foro":20}
n=ok=0
for u,s in zip(U,S):
    for a,b in zip(u["c"],s):
        n+=1; ok+= a==b
        if a!=b: print("DIFIERE",a,"|",b)
    if len(u["c"])!=len(s): print("CUENTA",u["id"],len(u["c"]),len(s))
print(f"Contenidos idénticos: {ok} de {n} (sílabo: {sum(map(len,S))})")
print(f"Componentes microproyecto: sitio {len(MP)} · sílabo {len(SMP)}")
for a,b in zip(MP,SMP): print("  ","=" if a.rstrip('.')==b.rstrip('.') else "≈",a,"|",b)
w={e[0]:int(re.search(r'\((\d+) %\)',e[1]).group(1)) for e in EV}
print("Pesos evaluación:",w,"coinciden" if w==SEV else "NO coinciden","· suma",sum(w.values()))
