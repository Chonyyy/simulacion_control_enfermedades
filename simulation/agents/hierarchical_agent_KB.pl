
%---------------------------- Paterns of Behaviour -----------------------------------------------

mascarilla(Agente, false).
mascarilla(Agente, true).

sintomas_enfermedad([tos, catarro, fiebre, dolor_de_cabeza]).
mis_sintomas([tos]).
hospitals([1,2]).

sintomas_presentes(Agente, [Sintomas]).
mantener_distanciamiento(Agente).
necesidad_comunicacion(Agente, OtroAgente, Informacion).
enviar_mensaje(Agente, OtroAgente, Informacion).
cambio_politicas_detectado(Agente, Cambio).
ajustar_comportamiento(Agente, Cambio).
recibir_notificacion(Agente, Notificacion).
ajustar_comportamiento(Agente, Notificacion).
necesidad_recurso(Agente, Recurso).
enviar_solicitud(Agente, Recurso).
contactos_riesgo_detectados(Agente, Contactos).
informar_contactos(Agente, Contactos).
necesidad_aislamiento(Agente).
usar_equipos_proteccion(Agente).
quedarse_en_casa(Agente).

usar_mascarilla(Agente):-
    mascarilla(Agente, true).

quitar_mascarilla(Agente):-
    mascarilla(Agente, false).

buscar_atencion_medica(Agente, move, Id):-
    hospitals(Id).

detectar_sintomas(Agente, Sintomas, X) :-
    sintomas_presentes(Agente, Sintomas),
    sintomas_enfermedad(SintomasEnfermedad),
    intersection(Sintomas, SintomasEnfermedad, SintomasComunes),
    SintomasComunes \= [],
    buscar_atencion_medica(Agente, X, Id).

implementar_medidas_prevencion(Agente) :-
    usar_mascarilla(Agente),
    mantener_distanciamiento(Agente).

comunicar_informacion(Agente, OtroAgente, Informacion) :-
    necesidad_comunicacion(Agente, OtroAgente, Informacion),
    enviar_mensaje(Agente, OtroAgente, Informacion).

ajustar_politicas_salud(Agente) :-
    cambio_politicas_detectado(Agente, Cambio),
    ajustar_comportamiento(Agente, Cambio).

responder_notificacion_autoridades(Agente, Notificacion) :-
    recibir_notificacion(Agente, Notificacion),
    ajustar_comportamiento(Agente, Notificacion).

solicitar_recursos_salud(Agente, Recurso) :-
    necesidad_recurso(Agente, Recurso),
    enviar_solicitud(Agente, Recurso).

seguimiento_contactos_riesgo(Agente) :-
    contactos_riesgo_detectados(Agente, Contactos),
    informar_contactos(Agente, Contactos).

implementar_medidas_aislamiento(Agente) :-
    necesidad_aislamiento(Agente),
    usar_equipos_proteccion(Agente),
    quedarse_en_casa(Agente).


%---------------------------- Local Plans --------------------------------------------------------

healthy(none).
quarantined(none).

% Behavior patterns for healthy citizens
healthy_citizen_behavior(social_distancing).
healthy_citizen_behavior(wearing_mask).

% Behavior patterns for infected citizens
infected_citizen_behavior(isolation).
infected_citizen_behavior(seeking_medical_help).

% Behavior patterns for citizens in quarantine
quarantined_citizen_behavior(stay_home).
quarantined_citizen_behavior(wearing_mask).

% Rule to determine behavior based on health status
behavior(Citizen, Behavior) :-
    healthy(Citizen),
    healthy_citizen_behavior(Behavior).

behavior(Citizen, Behavior) :-
    infected(Citizen),
    infected_citizen_behavior(Behavior).

behavior(Citizen, Behavior) :-
    quarantined(Citizen),
    quarantined_citizen_behavior(Behavior).



:-dynamic(infected/1).





%---------------------------- Cooperation Knowledge -----------------------------------------------




%--------------------------- Medotos auxiliares -----------------------------------------

intersection([], _, []).
intersection([H|T], L, [H|R]) :-
    member(H, L),
    intersection(T, L, R).
intersection([H|T], L, R) :-
    \+ member(H, L),
    intersection(T, L, R).
