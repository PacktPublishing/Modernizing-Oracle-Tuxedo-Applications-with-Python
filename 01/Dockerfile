FROM oraclelinux:8.2

RUN yum -y install oracle-release-el8 && \
    yum -y install \
           libnsl java-devel gcc-c++ python3-devel \ 
           unzip file hostname which sudo && \
    rm -rf /var/cache/yum 

RUN groupadd oracle && \
        useradd -m -g oracle -s /bin/bash oracle && \
        echo 'oracle ALL=(ALL) NOPASSWD:ALL' \
        >> /etc/sudoers.d/oracle

USER oracle

COPY tuxedo1222.rsp tuxedo122200_64_Linux_01_x86.zip /home/oracle/

ENV ORACLE_HOME=/home/oracle/tuxhome
ENV JAVA_HOME=/etc/alternatives/java_sdk

RUN cd ~/ && \
      jar xf tuxedo122200_64_Linux_01_x86.zip && \
      cd ~/Disk1/install && \
      chmod -R +x * && \
      ./runInstaller.sh -responseFile ~/tuxedo1222.rsp \
            -silent -waitforcompletion && \
      rm -rf ~/Disk1 && \
      rm -f ~/tuxedo1222.rsp ~/tuxedo122200_64_Linux_01_x86.zip

ENV TUXDIR=/home/oracle/tuxhome/tuxedo12.2.2.0.0
ENV PATH=$PATH:$TUXDIR/bin
ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$TUXDIR/lib

USER root
RUN pip3 install tuxedo

USER oracle

EXPOSE 5020
WORKDIR /home/oracle
