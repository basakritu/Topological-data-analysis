%% Rituparna's G2 of photoelastic images code (function Jie_Gsquare from Behringer lab in following section)

% Import the image of interest:
read_direct = 'C:\Users\ritup\Downloads\09_30_2019\';
read_dir='C:\Users\ritup\Downloads\G2perprt\';
imgg=zeros(size(img);
for i=2:7
        prefix='pimage0000';
        prefix2='_g2perprt';
        img=strcat(read_direct, prefix, num2str(i), '.jpg');
        final_p=imread(img);
        q=strcat(read_dir,prefix, num2str(i), prefix2,'.txt');
        centers_usep=importdata(q);
  
%final_p
% Import centers and radii of particles:
%centers_usep;
%centers_usep=importdata('C:\Users\ritup\Downloads\G2perprt\pimage00024_g2perprt.txt');
    
% Obtain G2 of image. Because your images have annular masks, edge pixels of cell may be slightly adversely affected:
[~,g2_p] = Jie_Gsquare(final_p); %g2_p is a DOUBLE, by the way. Convert back to Uint8 after re-scaling if you want to use this image

% Go through each particle, find avg G2 per pixel of particle area. Consider also shrinking radius by certain percentage or number of pixels to avoid edge brightness (edge diffraction) of grains:
g2perprt = zeros(length(centers_usep),1);

for ll = 1:length(centers_usep)
    pix = 0;
    g2 = 0;
    for xx = round(centers_usep(ll,1)-centers_usep(ll,3)):round(centers_usep(ll,1)+centers_usep(ll,3))
        for yy = round(centers_usep(ll,2)-centers_usep(ll,3)):round(centers_usep(ll,2)+centers_usep(ll,3))
            if (xx-centers_usep(ll,1))^2 + (yy-centers_usep(ll,2))^2 <= centers_usep(ll,3)^2
                pix = pix+1;
                g2 = g2 + g2_p(yy,xx);
            end
        end
    end
    g2perprt(ll) = g2/pix;
end

final_vector = [centers_usep,g2perprt]; % This is the array I gave you for each image.
i=i+1;
end
% Do what you wish for producing images!


%% G2 function

function [Gsquare,GradI] = Jie_Gsquare(pimg2)
% Input an image (can be double).
% Outputs:
%   Gsquare = avg G2 (per pixel) of entire image - not useful for us.
%   GradI = G2 image (G2 at each pixel); Double image.

%pimg2 = 'C:\Users\ritup\Downloads\09_30_2019\pimage00009.jpg';
for i=2:7
[vert, horz] = size(pimg2);
GradI=NaN(vert,horz);

Apadj = double(pimg2);

GradI(1,1)=1/3*(((Apadj(2,1)-Apadj(1,1))^2)/4+...
    ((Apadj(1,2)-Apadj(1,1))^2)/4+((Apadj(2,2)-Apadj(1,1))^2)/8);
GradI(vert,1)=1/3*(((Apadj(vert-1,1)-Apadj(vert,1))^2)/4+...
    ((Apadj(vert,2)-Apadj(vert,1))^2)/4+((Apadj(vert-1,2)-Apadj(vert,1))^2)/8);
GradI(1,horz)=1/3*(((Apadj(2,horz)-Apadj(1,horz))^2)/4+...
    ((Apadj(1,horz-1)-Apadj(1,horz))^2)/4+((Apadj(2,horz-1)-Apadj(1,horz))^2)/8);
GradI(vert,horz-6)=1/3*(((Apadj(vert-1,horz)-Apadj(vert,horz))^2)/4+...
    ((Apadj(vert,horz-1)-Apadj(vert,horz))^2)/4+((Apadj(vert-1,horz-1)-Apadj(vert,horz))^2)/8);

for i=2:vert-1
    GradI(i,1)=1/4*(((Apadj(i+1,1)-Apadj(i-1,1))^2)/4+((Apadj(i,2)-Apadj(i,1))^2)/4+...
        ((Apadj(i+1,2)-Apadj(i,1))^2)/8+((Apadj(i,1)-Apadj(i-1,2))^2)/8);
    GradI(i,horz)=1/4*(((Apadj(i+1,horz)-Apadj(i-1,horz))^2)/4+((Apadj(i,horz)-Apadj(i,horz-1))^2)/4+...
        ((Apadj(i,horz)-Apadj(i-1,horz-1))^2)/8+((Apadj(i+1,horz-1)-Apadj(i,horz))^2)/8);
end

for j=2:horz-1
    GradI(1,j)=1/4*(((Apadj(2,j)-Apadj(1,j))^2)/4+((Apadj(1,j+1)-Apadj(1,j-1))^2)/4+...
        ((Apadj(2,j+1)-Apadj(1,j))^2)/8+((Apadj(2,j-1)-Apadj(1,j))^2)/8);
    GradI(vert,j)=1/4*(((Apadj(vert,j)-Apadj(vert-1,j))^2)/4+((Apadj(vert,j+1)-Apadj(vert,j-1))^2)/4+...
        ((Apadj(vert,j)-Apadj(vert-1,j-1))^2)/8+((Apadj(vert,j)-Apadj(vert-1,j+1))^2)/8);
end

for j=2:horz-1
    for i=2:vert-1
        GradI(i,j)=1/4*(((Apadj(i+1,j)-Apadj(i-1,j))^2)/4+((Apadj(i,j+1)-Apadj(i,j-1))^2)/4+...
            ((Apadj(i+1,j+1)-Apadj(i-1,j-1))^2)/8+((Apadj(i+1,j-1)-Apadj(i-1,j+1))^2)/8);
    end
end
Gsquare=(nansum(nansum(GradI)))/(horz*vert);
write_name = strcat('C:\Users\ritup\Downloads\image\', num2str(i),'.png');
imwrite(GradI,write_name,'BitDepth',8);
imshow(GradI)
end
end

