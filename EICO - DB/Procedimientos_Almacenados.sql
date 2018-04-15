

#procedure encargado de hacer el inicio de sesión, dado un usuario y contraseña
delimiter $$
create procedure iniciar_sesion(correo_electronico varchar(40), contrasena varchar(50))

begin
	select u.id, tu.id as 'id_tipo_usuario', tu.nombre from Usuario u, Tipo_Usuario tu
    where u.correo_electronico = correo_electronico and u.contrasena = contrasena
    and tu.id = u.tipo_usuario_fk;
end $$
delimiter ;



#crud sitios de interés
##################################################################################

#c
delimiter $$
create procedure insertar_sitio_interes(titulo varchar(100), contenido text)
begin
	insert into Sitio_Interes(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;

#r
delimiter $$
create procedure obtener_sitios_interes()
begin
	select * from Sitio_Interes;
end $$
delimiter ;



#u
delimiter $$
create procedure editar_sitio_interes(id int, titulo varchar(100), contenido text)
begin
	update Sitio_Interes set Sitio_Interes.titulo = titulo, Sitio_Interes.contenido = contenido
    where Sitio_Interes.id = id;
end $$
delimiter ;



#d
delimiter $$
create procedure eliminar_sitio_interes(id int)
begin
	delete from Sitio_Interes where Sitio_Interes.id = id;
end $$
delimiter ;

##################################################################################


#crud servicios
##################################################################################

#c
delimiter $$
create procedure insertar_servicio(titulo varchar(100), contenido text)
begin
	insert into Servicio(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;

#r
delimiter $$
create procedure obtener_servicios()
begin
	select * from Servicio;
end $$
delimiter ;

#u
delimiter $$
create procedure editar_servicio(id int, titulo varchar(100), contenido text)
begin
	update Servicio set Servicio.titulo = titulo, Servicio.contenido = contenido
    where Servicio.id = id;
end $$
delimiter ;

#d
delimiter $$
create procedure eliminar_servicio(id int)
begin
	delete from Servicio where Servicio.id = id;
end $$
delimiter ;


##################################################################################


#inserta un nuevo tipo de usuario (estudiante, director, administrador, egresado, funcionario)
delimiter $$
create procedure insertar_tipo_usuario(nombre varchar(13))
begin
	insert into Tipo_Usuario(nombre) values(nombre);
end $$
delimiter ;


#inserta tipo de calificación (relevante, indiferente, emocionante)
delimiter $$
create procedure insertar_tipo_calificacion(nombre varchar(13))
begin
	insert into Tipo_Calificacion(nombre) values(nombre);
end $$
delimiter ;



delimiter $$
create procedure insertar_usuario(nombre_usuario varchar(50), contrasena varchar(50), correo_electronico varchar(40), titulo varchar(100), profesion varchar(100), lugar_trabajo varchar(200), media text, tipo_usuario_fk int)
begin
	insert into Usuario(nombre_usuario, contrasena, correo_electronico, titulo, profesion, lugar_trabajo, media, tipo_usuario_fk) values(nombre_usuario, contrasena, correo_electronico, titulo, profesion, lugar_trabajo, media, tipo_usuario_fk);
end $$
delimiter ;

select * from Usuario;


delimiter $$
create procedure obtener_id_tipo_usuario(nombre varchar(13))

begin
	select tu.id from Tipo_Usuario tu
    where tu.nombre = nombre;
end $$
delimiter ;

delimiter $$
create procedure obtener_publicaciones_egresados()

begin
	select p.titulo, p.descripcion, p.fecha, p.media, p.link_video, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre = 'Egresado';
end $$
delimiter ;

delimiter $$
create procedure obtener_publicaciones_escuela()

begin
	select p.titulo, p.descripcion, p.fecha, p.media, p.link_video, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre <> 'Egresado';
end $$
delimiter ;

delimiter $$

create procedure insertar_publicacion(titulo varchar(100), descripcion text, link_video text, media text,  usuario_fk int)

begin
	insert into Publicacion(titulo, descripcion, link_video,  fecha, media, usuario_fk) values (titulo, descripcion, link_video, CURDATE(), media, usuario_fk);
end $$
delimiter ;


