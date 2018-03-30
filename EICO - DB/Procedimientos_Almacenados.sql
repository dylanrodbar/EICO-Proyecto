#Procedure encargado de hacer el inicio de sesión, dado un usuario y contraseña
delimiter $$
create procedure iniciar_sesion(correo_electronico varchar(40), contrasena varchar(50))

begin
	select u.id, tu.id as 'id_tipo_usuario', tu.nombre from Usuario u, Tipo_Usuario tu
    where u.correo_electronico = correo_electronico and u.contrasena = contrasena
    and tu.id = u.tipo_usuario_fk;
end $$
delimiter ;

delimiter $$
create procedure insertar_sitio_interes(titulo varchar(100), contenido text)
begin
	insert into Sitio_Interes(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;


delimiter $$
create procedure insertar_media(link text, tipo_media_fk int)
begin
	insert into Media(link, tipo_media_fk) values(link, tipo_media_fk);
end $$
delimiter ;

delimiter $$
create procedure obtener_media(id int)
begin
	select * from Media where Media.id = id;
end $$
delimiter ;


delimiter $$
create procedure editar_sitio_interes(id int, titulo varchar(100), contenido text)
begin
	update Sitio_Interes set Sitio_Interes.titulo = titulo, Sitio_Interes.contenido = contenido
    where Sitio_Interes.id = id;
end $$
delimiter ;

delimiter $$
create procedure eliminar_sitio_interes(id int)
begin
	delete from Sitio_Interes where Sitio_Interes.id = id;
end $$
delimiter ;

delimiter $$
create procedure obtener_sitios_interes()
begin
	select * from Sitio_Interes;
end $$
delimiter ;

call obtener_sitios_interes
##


delimiter $$
create procedure editar_servicio(id int, titulo varchar(100), contenido text)
begin
	update Servicio set Servicio.titulo = titulo, Servicio.contenido = contenido
    where Servicio.id = id;
end $$
delimiter ;

delimiter $$
create procedure eliminar_servicio(id int)
begin
	delete from Servicio where Servicio.id = id;
end $$
delimiter ;

delimiter $$
create procedure obtener_servicios()
begin
	select * from Servicio;
end $$
delimiter ;
##






delimiter $$
create procedure insertar_servicio(titulo varchar(100), contenido text)
begin
	insert into Servicio(titulo, contenido) values(titulo, contenido);
end $$
delimiter ;



delimiter $$
create procedure insertar_tipo_usuario(nombre varchar(13))
begin
	insert into Tipo_Usuario(nombre) values(nombre);
end $$
delimiter ;



delimiter $$
create procedure insertar_tipo_calificacion(nombre varchar(13))
begin
	insert into Tipo_Calificacion(nombre) values(nombre);
end $$
delimiter ;




delimiter $$
create procedure insertar_tipo_media(nombre varchar(13))
begin
	insert into Tipo_Media(nombre) values(nombre);
end $$
delimiter ;




delimiter $$
create procedure insertar_tipo_formacion(nombre varchar(13))
begin
	insert into Tipo_Formacion(nombre) values(nombre);
end $$
delimiter ;

delimiter $$
create procedure insertar_usuario(nombre_usuario varchar(50), contrasena varchar(50), correo_electronico varchar(40), media_fk int, tipo_usuario_fk int)
begin
	insert into Usuario(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk) values(nombre_usuario, contrasena, correo_electronico, media_fk, tipo_usuario_fk);
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
	select p.titulo, p.descripcion, p.fecha, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre = 'Egresado';
end $$
delimiter ;

delimiter $$
create procedure obtener_publicaciones_escuela()

begin
	select p.titulo, p.descripcion, p.fecha, u.nombre_usuario from Publicacion p, Usuario u, Tipo_Usuario tu
    where p.usuario_fk = u.id and u.tipo_usuario_fk = tu.id and tu.nombre <> 'Egresado';
end $$
delimiter ;

delimiter $$
create procedure insertar_publicacion(titulo varchar(100), descripcion text, usuario_fk int)

begin
	insert into Publicacion(titulo, descripcion, fecha, usuario_fk) values (titulo, descripcion, CURDATE(), usuario_fk);
end $$
delimiter ;


call obtener_sitios_interes
call obtener_servicios
